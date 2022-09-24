from moviepy.editor import *
from tkinter import *
from tkinter import filedialog
import os

main = Tk()
main.geometry("630x500+400+100")
main.title("video2audio")
main.configure(bg="#00ffff")


def browse_file():
    global file
    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="select file",filetype=(("Video Files", ".mp4"), ("All Files", "*.*")))

def get_mp4():
    clip = VideoFileClip(file)
    audio = clip.audio
    audio.write_audiofile("audio.mp3")


Button(main, text="SELECT VIDEO", command=browse_file, width=15, font="arial 20", bg="orange", bd=4).place(x=40, y=100)
Button(main, text="CONVERT AUDIO", command=get_mp4, width=15, font="arial 20", bg="red",  bd=4).place(x=330, y=100)


main.mainloop()

#*.WEBM, *.MPG, *.MP2,*.MPEG, *.MPE, *.MPV, *.OGG,*.MP4,*.M4P, *.M4V, *.AVI, *.WMV,*.MOV, *.QT,*.FLV, *.SWF,