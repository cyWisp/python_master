#!/usr/bin/env python
from os import path, makedirs
from sys import exit
from zipfile import ZipFile

if __name__ == '__main__':

    dest = "C:\\youtube_dl"
    zip_file = "./p.zip"

    files = [
        'ffmpeg.exe',
        'ffplay.exe',
        'ffprobe.exe',
        'youtube-dl.exe',
    ]

    if not path.exists(dest):
        makedirs(dest)
    else:
        pass

    with ZipFile(zip_file) as zip_var:
        zip_var.extractall(dest)
            
    print("[*] Done...")
    exit(0)

    