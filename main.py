from moviepy.editor import *

clip = VideoFileClip("videoplayback.mp4")

# from tkinter.filedialog import *
#
# video = askopenfile()
#
# vdo = moviepy.editor.VideoClip
#
audio = clip.audio
#
audio.write_audiofile("audio.mp3")