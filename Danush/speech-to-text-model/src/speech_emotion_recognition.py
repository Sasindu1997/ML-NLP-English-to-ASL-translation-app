import contextlib
import wave

# librosa is a Python library for analyzing audio and music. It can be used to extract the data from the audio files
# we will see it later.
import librosa
import librosa.display
import numpy as np
import pandas as pd
from tensorflow import keras


# import warnings
# if not sys.warnoptions:
#     warnings.simplefilter("ignore")
# warnings.filterwarnings("ignore", category=DeprecationWarning)

def write_wave(path, audio, sample_rate):
    """Writes a .wav file.
    Takes path, PCM audio data, and sample rate.
    """
    with contextlib.closing(wave.open(path, 'wb')) as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio)


def run_model(path_to_wav):
    reconstructed_model = keras.models.load_model("my_ser_model")
    # reconstructed_model.summary()

    # Paths for data.
    # path_to_voiced_wavs = "./temp/"
    #
    # path_to_voiced_wavs_directory_list = os.listdir(path_to_voiced_wavs)
    #
    # print(path_to_voiced_wavs_directory_list)

    file_emotion = []
    file_path = [path_to_wav]

    file_emotion.append('neutral')
    # for file in path_to_voiced_wavs_directory_list:
    #     file_path.append(path_to_voiced_wavs + file)
    #     file_emotion.append('neutral')

    # dataframe for emotion of files
    emotion_df = pd.DataFrame(file_emotion, columns=['Emotions'])

    # dataframe for path of files.
    path_df = pd.DataFrame(file_path, columns=['Path'])
    voiced_wavs_df = pd.concat([emotion_df, path_df], axis=1)
    voiced_wavs_df.head()

    # creating Dataframe using all the 4 dataframes we created so far.
    data_path = pd.concat([voiced_wavs_df], axis=0)
    data_path.to_csv("data_path.csv", index=False)
    data_path.head()

    # taking any example and checking for techniques.
    path = np.array(data_path.Path)[0]
    data, sample_rate = librosa.load(path)

    # Functions
    def noise(data):
        noise_amp = 0.035 * np.random.uniform() * np.amax(data)
        data = data + noise_amp * np.random.normal(size=data.shape[0])
        return data

    def stretch(data, rate=0.8):
        return librosa.effects.time_stretch(data, rate)

    def shift(data):
        shift_range = int(np.random.uniform(low=-5, high=5) * 1000)
        return np.roll(data, shift_range)

    def pitch(data, sampling_rate, pitch_factor=0.7):
        return librosa.effects.pitch_shift(data, sampling_rate, pitch_factor)

    def extract_features(data):
        # ZCR
        result = np.array([])
        zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
        result = np.hstack((result, zcr))  # stacking horizontally

        # Chroma_stft
        stft = np.abs(librosa.stft(data))
        chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
        result = np.hstack((result, chroma_stft))  # stacking horizontally

        # MFCC
        mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate).T, axis=0)
        result = np.hstack((result, mfcc))  # stacking horizontally

        # Root Mean Square Value
        rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
        result = np.hstack((result, rms))  # stacking horizontally

        # MelSpectogram
        mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
        result = np.hstack((result, mel))  # stacking horizontally

        return result

    def get_features(path_to_audio_file):
        # duration and offset are used to take care of the no audio in start and the ending of each audio files as
        # seen above.
        data, sample_rate = librosa.load(path_to_audio_file, duration=2.5, offset=0.6)

        # without augmentation
        res1 = extract_features(data)
        result = np.array(res1)

        # data with noise
        noise_data = noise(data)
        res2 = extract_features(noise_data)
        result = np.vstack((result, res2))  # stacking vertically

        # data with stretching and pitching
        new_data = stretch(data)
        data_stretch_pitch = pitch(new_data, sample_rate)
        res3 = extract_features(data_stretch_pitch)
        result = np.vstack((result, res3))  # stacking vertically

        return result

    X, Y = [], []
    for path, emotion in zip(data_path.Path, data_path.Emotions):
        feature = get_features(path)
        for ele in feature:
            X.append(ele)
            # appending emotion 3 times as we have made 3 augmentation techniques on each audio file.
            Y.append(emotion)

    Features = pd.DataFrame(X)
    Features['labels'] = Y
    Features.to_csv('features.csv', index=False)
    Features.head()

    X = Features.iloc[:, :-1].values
    Y = Features['labels'].values

    import pickle
    # open a file, where you stored the pickled data
    file = open('encoder', 'rb')

    # dump information to that file
    encoder = pickle.load(file)

    # close the file
    file.close()

    x_test = X
    y_test = Y

    x_test.shape, y_test.shape

    # making our data compatible to model.
    # x_train = np.expand_dims(x_train, axis=2)
    x_test = np.expand_dims(x_test, axis=2)
    # x_train.shape, y_train.shape,
    x_test.shape, y_test.shape

    # predicting on test data.
    pred_test = reconstructed_model.predict(x_test)
    y_pred = encoder.inverse_transform(pred_test)

    # print(y_pred)
    # print(y_pred[0][0])

    return y_pred[0][0]


def recognize_emotion(path_to_wav):
    result = run_model(path_to_wav)
    # print(result)
    return result


# def recognize_emotion():
#     result = run_model()
#     print(result)
#     return result


if __name__ == '__main__':
    recognize_emotion()
