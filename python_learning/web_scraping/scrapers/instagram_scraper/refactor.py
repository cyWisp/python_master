from tkinter import *
from sys import argv, exit
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import os, cv2, json, requests, urllib.request, tkinter as tk

TARGET_DIR = "./"

def get_args():

    if len(argv) != 2:
        print(f"[!] Usage: {argv[0]} <post URL>")
        exit(0)
    else:
        print(f"{TARGET_DIR}")
        return argv[1]


def i_Downloader():
    
    
    
    insta_Posts = requests.get(instaURL.get())
 
    soup = BeautifulSoup(insta_Posts.text, 'html.parser')
    
    script = soup.find('script', text=re.compile('window._sharedData'))
    
    page_json = script.text.split(' = ', 1)[1].rstrip(';')
    
    data = json.loads(page_json)
    
    base_data = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    
    typename = base_data['__typename']

if __name__ == '__main__':

    url = get_args()