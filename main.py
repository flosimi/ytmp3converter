#video.mov files cpnvert to mp3
import subprocess
import os

def convert_to_mp3(input_file,output_file):
    ffmpeg_cmd=[
        "ffmpeg",
        "-i",input_file,
        "-vn",
        "-acodec","libmp3lame",
        "-ab","192k",
        "-ar","44100",
        "-y",
        output_file
    ]
    try:
        subprocess.run(ffmpeg_cmd,check=True)
    except subprocess.CalledProcessError as e:
        print("Conversion failed! ")

convert_to_mp3("Moves Like Jagger.mp4","audio.mp3")
