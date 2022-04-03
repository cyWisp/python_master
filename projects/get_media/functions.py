#!/usr/bin/env python
from subprocess import Popen, PIPE

def get_command(script_args):
    print("[+] Building youtube-dl command...")
    if script_args.audio_switch: command = f"youtube-dl --extract-audio --audio-format mp3 {script_args.arg_list[2]}"
    else: command = f"youtube-dl {script_args.arg_list[1]}"
    return command

def run_youtube_dl(command):
    print("[+] Running youtube-dl with specified parameters...")
    com = Popen([command], shell=True, stdout=PIPE, stderr=PIPE)
    com.wait()
    
    output = com.communicate()[0].decode('utf-8')
    error = com.communicate()[1].decode('utf-8')

    if error != "\n": print("[+] Download Successful!")
    else: print(f"[x] Error: {error}")