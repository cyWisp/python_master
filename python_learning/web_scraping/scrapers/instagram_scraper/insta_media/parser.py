#!/usr/bin/env python
import os, re, json, requests
from bs4 import BeautifulSoup
from functions import check_path
from urllib.request import urlopen, urlretrieve

def parse_data(html):

    soup = BeautifulSoup(html, 'html.parser')
    shared_data = soup.find('script', text=re.compile('window._sharedData'))
    json_raw = shared_data.text.split(' = ', 1)[1].rstrip(';')
    raw_data = json.loads(json_raw)
    base_data = raw_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    type_name = base_data['__typename']

    return base_data, type_name

def get_graph_image(base_data, download_path):

    display_url, file_name = base_data['display_url'], base_data['taken_at_timestamp']    
    download_file_name = f"{download_path}{str(file_name)}.jpg"
    urlretrieve(display_url, check_path(download_file_name))

def get_graph_video(base_data, download_path):

    video_url, file_name = base_data['video_url'], base_data['taken_at_timestamp']
    download_file_name = f"{download_path}{str(file_name)}.mp4"
    urlretrieve(video_url, check_path(download_file_name))

def get_graph_sideCar(base_data, download_path):
    response = requests.get(f"https://www.instagram.com/p/" + base_data['shortcode'] + "/?__a=1").json()

    


