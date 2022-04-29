# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip(r"C:\Users\DELL\Desktop\RP\ML-NLP-Model-for-English-to-ASL-translation\VideoFiles\i.mp4")
clip1 = VideoFileClip(r"C:\Users\DELL\Desktop\RP\ML-NLP-Model-for-English-to-ASL-translation\VideoFiles\go.mp4")
clip2 = VideoFileClip(r"C:\Users\DELL\Desktop\RP\ML-NLP-Model-for-English-to-ASL-translation\VideoFiles\home.mp4")

# clip list
clips = [clip, clip1, clip2]

# concatenating both the clips
final = concatenate_videoclips(clips, method='compose')

# showing final clip
final.ipython_display(width=480)
