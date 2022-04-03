#!/usr/bin/env python
from tkinter import *
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import os, cv2, json, requests, urllib.request
from urllib.request import urlopen, urlretrieve


def test_requests(url):
    return requests.get(url)

def test_urlopen(url):
    return urlopen(url)

if __name__ == '__main__':

    #url = "http://cybersherpa.net"
    link = "https://www.instagram.com/p/B5-SLItArU6/"

    #print(f"requests.get(): {test_requests(url).text}")
    #print(f"urlopen: {test_urlopen(link).read()}\n\n\n")

    download_path = "./"
    response_1 = urlopen(link).read()
    #response_2 = requests.get(link).text
    # print(response_2)
    soup = BeautifulSoup(response_1, 'html.parser')
    script = soup.find('script', text=re.compile('window._sharedData'))
    #print(script)

    json_var = script.text.split(' = ', 1)[1].rstrip(';')
    #print(json_var)
    data = json.loads(json_var)
    # base_data is a dictionary 
    base_data = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    #base data __type_name
    type_name = base_data['__typename']

    #print(type_name)

    if type_name == 'GraphImage':
        # image url from display_url in base_data directory
        display_url = base_data['display_url']
        # get the file_name from the taken_at_timestamp_value from base_data dict
        file_name = base_data['taken_at_timestamp']
        # defining the download path
        download_p = f"{download_path}.jpg"

    


