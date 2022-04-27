# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip(os.path.join("VideoFiles", "hello.mp4"))

# # getting subclip as video is large
# clip1 = clip.subclip(0, 5)
#
# # getting subclip as video is large
# clip2 = clip.subclip(60, 65)
#
# # concatenating both the clips
# final = concatenate_videoclips([clip1, clip2])
# #writing the video into a file / saving the combined video
# final.write_videofile("merged.webm")
#
# # showing final clip
clip.ipython_display(width = 480)
