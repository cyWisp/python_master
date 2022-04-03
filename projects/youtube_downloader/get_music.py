#!/usr/bin/env python
import sys, os, time

def check_args(script_arguments):

    if script_arguments is not 2:
        print("[!] Usage: python {0} <url>".format(sys.argv[0]))
        sys.exit(0)
    else:
        pass

def download_video(url):

    print("[*] Now Downloading...")
    os.system("youtube-dl --extract-audio --audio-format mp3 {0}".format(url))
    print("[*] Done...")

if __name__ == '__main__':

    os.system("clear")
    time.sleep(1)

    print("[*] Youtube Downloader V3")

    check_args(len(sys.argv))
    download_video(sys.argv[1])
    sys.exit(0)
