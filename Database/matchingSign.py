# imports
from tinydb import TinyDB, Query
from AudioData.getAudioData import getAudioRecord
from NLTK.testModel1 import *
from VideoProcessing.videoProcessing import processFinalVideo, outputFinalVideo

# importing vlc module
import vlc

# importing tkinter module
from tkinter import *

# importing pafy module
import pafy

# defining database instance
db = TinyDB('db.json')
Sign = Query()

# defining tkinter instance
root = Tk()
root.geometry("800x500")
root.resizable(width=False, height=False)

# defining vlc instance
instance = vlc.Instance()
p = instance.media_player_new()
p.set_hwnd(root.winfo_id())

# defining video generation file location
url = r"C:\Users\DELL\Desktop\RP\ML-NLP-Model-for-English-to-ASL-translation\Database\__temp__.mp4"
p.set_media(instance.media_new(url))

matchedVideoURLArray = []

Input1 = 'hello! I am going home.'
Input2 = 'I home no.'

# input functions
inputArray = [Input1, Input2]
filename = "Recording1.wav"
recordedInput = getAudioRecord(filename)


# defining start function for processing

def startTextProcessingForSingleSentence(Input):
    result = testModelFunc(Input)
    print("result", result)

    def matchSignFromDatabase(searchParam):
        # print('searchParam', str(searchParam))
        res = db.search(Sign.name == searchParam)
        print('res', res)
        return res

    for word in result:
        results = matchSignFromDatabase(word)
        print('final', results)
        matchedVideoURLArray.append(results)

    clipsArray = processFinalVideo(matchedVideoURLArray, root, p)
    print('clipsArray', clipsArray)

    playVideoStatus = outputFinalVideo(clipsArray, root, p)

    return playVideoStatus


# calling start function for processing

startTextProcessingForSingleSentence(recordedInput)


# Looping start function for processing when give an array of inputs

# while len(inputArray):
#     newSentence = inputArray.pop(0)
#     print('*******************    index  *************************')
#     results = startTextprocessingForSingleSentence(newSentence)
#     matchedVideoURLArray = []
#     clipsArray = []
#     print('startTextprocessingForSingleSentence', results)
#
# inputArray.pop(0)


# continue tkinter instance

root.mainloop()
