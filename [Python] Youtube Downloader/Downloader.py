"""
Youtube Downloader made by. Mir Nanaichi
To use this, you need to install "moviepy" and "pytube" first.

// pip install pytube
// pip3 install moviepy

This Python code downloads automatically a highest quality of video.
"""

from pytube import YouTube, Playlist
from moviepy.editor import *
import glob
import os.path

def download(url, name):
    youtube = YouTube(url)

    video_path = (
        youtube.streams.filter(adaptive = True, file_extension = "mp4", only_video = True)
        .order_by("resolution")
        .desc()
        .first()
        .download('./video')
    )

    audio_path = (
        youtube.streams.filter(adaptive = True, file_extension = "mp4", only_audio = True)
        .order_by("abr")
        .desc()
        .first()
        .download('./audio')
    )

    v = VideoFileClip(video_path)
    a = AudioFileClip(audio_path)

    v.audio = a
    v.write_videofile(f"{name}.mp4")

adresse = input("Video URL: ")
filename = input("Enter new Filename: ")
download(adresse, filename)
