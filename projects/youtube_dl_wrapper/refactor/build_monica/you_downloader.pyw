#!/usr/bin/env python
from datetime import datetime
from sys import exit
from os import system, path, makedirs
import tkinter as tk
from tkinter import *
from tkinter import ttk
from time import sleep

def setup():

    if not path.exists('./downloads'):
        makedirs('./downloads')
    else:
        pass

def reset():
    sleep(3)
    action_label.configure(text="Ready...")
    clear_text()
    master.update()

def clear_text():
    url_text_box.delete(0, 'end')

def download_video():

    if url_text_var != '':
        video_url = url_text_var.get()
        command = f'youtube-dl --extract-audio --audio-format mp3 {video_url} -o "./downloads/%(title)s.%(ext)s"'
        system(command)
        action_label.configure(text='Video Downloaded at {0}'.format(datetime.now()))
        master.update()
        reset()
    else:
        action_label.configure('Please enter a valid url!')
        master.update()
        reset()

def update():
    action_label.configure(text=f'Checking for update at {datetime.now()}')
    master.update()
    command = 'youtube-dl --update'
    system(command)
    action_label.configure(text="Done...")
    master.update()
    reset()

if __name__ == '__main__':

    global master
    global title_label, url_text_var, url_text_box, download_button, exit_button, update_button

    setup()

    master = tk.Tk()
    master.minsize(300, 125)
    master.title("Monica's Youtube Downloader")

    title_label = ttk.Label(master, text="Monica's Downloader")
    title_label.place(x=95, y=5)

    url_text_var = tk.StringVar()
    url_text_box = ttk.Entry(master, width=40, textvariable=url_text_var)
    url_text_box.place(x=25, y=30)

    download_button = ttk.Button(master, text='Download', command=download_video)
    download_button.place(x=25, y=60)

    update_button = ttk.Button(master, text='Update', command=update)
    update_button.place(x=110, y=60)

    exit_button = ttk.Button(master, text='Exit', command=exit)
    exit_button.place(x=195, y=60)

    action_label = ttk.Label(master, text='Ready...')
    action_label.place(x=25, y=100)

    master.mainloop()
