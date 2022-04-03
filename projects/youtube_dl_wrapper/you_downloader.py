#!/usr/bin/env python
import sys, os, time
from datetime import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk

def download_video():

    if url_text_var != '':
        video_url = url_text_var.get()
        command = 'youtube-dl --extract-audio --audio-format mp3 {0}'.format(video_url)
        os.system(command)
        action_label.configure(text='Video Downloaded at {0}'.format(datetime.now()))
        master.update()
    else:
        action_label.configure('Please enter a valid url!')
        master.update()

def exit():

    sys.exit(0)

if __name__ == '__main__':

    global master
    global title_label, url_text_var, url_text_box, download_button, exit_button

    master = tk.Tk()
    master.minsize(300, 125)
    master.title("Mama's Youtube Downloader")

    title_label = ttk.Label(master, text="Mama's Downloader")
    title_label.place(x=95, y=5)

    url_text_var = tk.StringVar()
    url_text_box = ttk.Entry(master, width=40, textvariable=url_text_var)
    url_text_box.place(x=25, y=30)

    download_button = ttk.Button(master, text='Download', command=download_video)
    download_button.place(x=25, y=60)

    exit_button = ttk.Button(master, text='Exit', command=exit)
    exit_button.place(x=195, y=60)

    action_label = ttk.Label(master, text='Ready...')
    action_label.place(x=25, y=100)

    master.mainloop()
