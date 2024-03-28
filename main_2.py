#mp4 video to mp3 audio files
import moviepy.editor
from tkinter.filedialog import askopenfilename
import tkinter as tk

def convert_to_mp3():
    video_file = askopenfilename()
    video=moviepy.editor.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile("sample.mp3")
    print("Conversion Completed")
root = tk.Tk()
root.title("MP3 Converter")
root.geometry("900x260")
convert_button = tk.Button(root,text="Convert to mp3",command=convert_to_mp3)

convert_button.pack()

root.mainloop()
