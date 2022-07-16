import os
from pickle import FALSE, TRUE

os.add_dll_directory(os.getcwd())

# Import everything needed to edit video clips
from moviepy.editor import *

# Import everything needed to edit video clips
import vlc

# Import everything needed to edit video clips
import time

# loading video dsa gfg intro video
clipURL = r'C:\Users\DELL\Desktop\RP\ML-NLP-Model-for-English-to-ASL-translation\VideoFiles'
# clip = VideoFileClip(r"C:\Users\DELL\Desktop\RP\ML-NLP-Model-for-English-to-ASL-translation\VideoFiles\i.mp4")
# clip1 = VideoFileClip(r"C:\Users\DELL\Desktop\RP\ML-NLP-Model-for-English-to-ASL-translation\VideoFiles\go.mp4")
# clip2 = VideoFileClip(r"C:\Users\DELL\Desktop\RP\ML-NLP-Model-for-English-to-ASL-translation\VideoFiles\home.mp4")

# clip list
# clips = [clip, clip1, clip2]
#
# # concatenating both the clips
# final = concatenate_videoclips(clips, method='compose')
#
# # showing final clip
# final.ipython_display(width=480)

formattedarray = []

def processFinalVideo(VideoArray):
    try:
        print("VideoArray", VideoArray)
        list = [x for x in VideoArray if x != []]
        print("list2", list)

        for video in list:
            print("video", video[0]['path'])

            newURL = clipURL + "\\" + video[0]['path']
            print("video", newURL)

            formattedarray.append(VideoFileClip(newURL))
            print("formattedarray", formattedarray)

        list2 = [x for x in formattedarray if x != []]
        print("list2", list2)

        formattedarray.clear()
        return list2
    except:
        print("Err in processFinalVideo")
        return FALSE


def outputFinalVideo(newArray, player):


    try:
        print("called", newArray)
        final = concatenate_videoclips(newArray, method='compose')
        print("final", final)
        final.ipython_display(width=480)
        playFinalVideo(player)
        print("newArray is success.")
        newArray.clear()
        formattedarray.clear()
        return final
    except:
        print("Err in outputFinalVideo.")
        return FALSE


def playFinalVideo(player):
    try:
        # # play the video
        time.sleep(3)
        player.play()
        formattedarray.clear()
        print("playFinalVideo is success.")
        return TRUE

    except:
        print("Err in playFinalVideo")
        return FALSE
