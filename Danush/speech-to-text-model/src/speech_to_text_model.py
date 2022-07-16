import collections
import logging
import queue
import wave
from pathlib import Path

import deepspeech as ds
import numpy as np
import pyaudio
import tensorflow as tf
import vlc
import webrtcvad
from halo import Halo
from scipy import signal

# print('hello world!')
from Database.matchingSign import startTextProcessingForSingleSentence

from speech_emotion_recognition import write_wave, recognize_emotion

print(tf.__version__)

# default sampling rate
DEFAULT_SAMPLE_RATE = 16000


class VADAudio(object):
    """Audio stream is being filtered based on voice activity detection."""

    frame_duration_ms = property(
        lambda self: 1000 * self.block_size // self.sample_rate)

    FORMAT = pyaudio.paInt16
    # Network/VAD rate-space
    RATE_PROCESS = 16000
    CHANNELS = 1
    BLOCKS_PER_SECOND = 50

    def __init__(self, callback=None, device=None, input_rate=RATE_PROCESS, file=None, aggressiveness=3):
        def proxy_callback(in_data, frame_count, time_info, status):
            if self.chunk is not None:
                in_data = self.wf.readframes(self.chunk)
            callback(in_data)
            return None, pyaudio.paContinue

        if callback is None: callback = lambda in_data: self.buffer_queue.put(in_data)
        self.buffer_queue = queue.Queue()
        self.device = device
        self.dev_index = 2
        self.input_rate = input_rate
        self.sample_rate = self.RATE_PROCESS
        self.block_size = int(self.RATE_PROCESS / float(self.BLOCKS_PER_SECOND))
        self.block_size_input = int(self.input_rate / float(self.BLOCKS_PER_SECOND))
        self.pa = pyaudio.PyAudio()
        self.vad = webrtcvad.Vad(aggressiveness)

        # Get the input device index of the Stereo Mix
        for i in range(self.pa.get_device_count()):
            dev = self.pa.get_device_info_by_index(i)
            # print(dev)
            # and dev['hostApi'] == 0:
            if dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0:
                print('Stereo Mix channel identified !')
                self.dev_index = dev['index'];
                print('dev_index', self.dev_index)

        kwargs = {
            'format': self.FORMAT,
            'channels': self.CHANNELS,
            'rate': self.input_rate,
            'input': True,
            'input_device_index': self.dev_index,
            'frames_per_buffer': self.block_size_input,
            'stream_callback': proxy_callback,
        }

        self.chunk = None
        # if not default device
        if self.device:
            kwargs['input_device_index'] = self.device
        elif file is not None:
            self.chunk = 320
            self.wf = wave.open(file, 'rb')

        self.stream = self.pa.open(**kwargs)
        self.stream.start_stream()

    def resample(self, data, input_rate):
        """
        Microphone may not support our native processing sampling rate, so
        resample from input_rate to RATE_PROCESS here for webrtcvad.

        Args:
            data (binary): Input audio stream
            input_rate (int): Input audio rate to resample from
        """
        data16 = np.fromstring(string=data, dtype=np.int16)
        resample_size = int(len(data16) / self.input_rate * self.RATE_PROCESS)
        resample = signal.resample(data16, resample_size)
        resample16 = np.array(resample, dtype=np.int16)
        return resample16.tostring()

    def read_resampled(self):
        """Return a block of audio data resampled to 16000hz, blocking if necessary."""
        return self.resample(data=self.buffer_queue.get(),
                             input_rate=self.input_rate)

    def read(self):
        """Return a block of audio data, blocking if necessary."""
        return self.buffer_queue.get()

    def write_wav(self, filename, data):
        logging.info("write wav %s", filename)
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS)
        # wf.setsampwidth(self.pa.get_sample_size(FORMAT))
        assert self.FORMAT == pyaudio.paInt16
        wf.setsampwidth(2)
        wf.setframerate(self.sample_rate)
        wf.writeframes(data)
        wf.close()

    def frame_generator(self):
        """Generator that yields all audio frames from microphone."""
        if self.input_rate == self.RATE_PROCESS:
            while True:
                yield self.read()
        else:
            while True:
                yield self.read_resampled()

    def vad_collector(self, padding_ms=300, ratio=0.75, frames=None):
        """Generator that yields series of consecutive audio frames comprising each utterence, separated by yielding a single None.
            Determines voice activity by ratio of frames in padding_ms. Uses a buffer to include padding_ms prior to being triggered.
            Example: (frame, ..., frame, None, frame, ..., frame, None, ...)
                      |---utterence---|        |---utterence---|
        """
        if frames is None:
            frames = self.frame_generator()
        num_padding_frames = padding_ms // self.frame_duration_ms
        ring_buffer = collections.deque(maxlen=num_padding_frames)
        triggered = False

        for frame in frames:
            if len(frame) < 640:
                return

            is_speech = self.vad.is_speech(frame, self.sample_rate)

            if not triggered:
                ring_buffer.append((frame, is_speech))
                num_voiced = len([f for f, speech in ring_buffer if speech])
                if num_voiced > ratio * ring_buffer.maxlen:
                    triggered = True
                    for f, s in ring_buffer:
                        yield f
                    ring_buffer.clear()

            else:
                yield frame
                ring_buffer.append((frame, is_speech))
                num_unvoiced = len(
                    [f for f, speech in ring_buffer if not speech])
                if num_unvoiced > ratio * ring_buffer.maxlen:
                    triggered = False
                    yield None
                    ring_buffer.clear()


def main():
    # Load model
    model_path = str(Path('../models/my_model.pbmm').resolve())
    scorer = str(Path('../models/my_model_scorer.scorer').resolve())

    print('Initializing model...')
    print("model: %s", model_path)
    model = ds.Model(model_path)
    if scorer:
        print("scorer: %s", scorer)
        model.enableExternalScorer(scorer)

    # Start audio with VAD
    vad_audio = VADAudio(aggressiveness=3,
                         device=None,
                         input_rate=DEFAULT_SAMPLE_RATE,
                         file=None)
    print("Listening (Press ctrl-C to exit)...")

    # frames means 'segments'
    frames = vad_audio.vad_collector()

    # Stream from microphone to ds using VAD
    spinner = Halo(spinner='line')
    stream_context = model.createStream()
    wav_data = bytearray()

    i = 0
    voiced_frames = []

    # defining vlc instance
    instance = vlc.Instance(['--video-on-top'])
    player = instance.media_player_new()
    # p.set_hwnd(root.winfo_ide location())
    #     player.set_xwindow(display.winfo_id())
    #     # defining video generation fil
    url = r"C:\Users\DELL\Desktop\RP\ML-NLP-Model-for-English-to-ASL-translation\Danush\speech-to-text-model\src\__temp__.mp4"
    player.set_media(instance.media_new(url))


    for frame in frames:
        if frame is not None:
            if spinner:
                spinner.start()
            stream_context.feedAudioContent(np.frombuffer(frame, np.int16))
            voiced_frames.append(frame)


        else:
            if spinner:
                spinner.stop()
            print("end utterance")
            text = stream_context.finishStream()
            path = './temp/chunk-%002d.wav' % (i,)
            print('Writing %s' % (path,))
            write_wave(path, b''.join([f for f in voiced_frames]), 16000)
            recognized_emotion = recognize_emotion(path)
            i = i + 1

            print("Recognized Emotion: %s" % recognized_emotion)

            print("Recognized: %s" % text)

            # Calling text to ASL Translation model
            if text: startTextProcessingForSingleSentence(text, player)
            # player.vlm_del_media(url)

            stream_context = model.createStream()


if __name__ == '__main__':
    DEFAULT_SAMPLE_RATE = 16000
    main()
