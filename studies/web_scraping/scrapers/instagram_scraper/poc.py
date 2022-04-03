#!/usr/bin/env python
from tkinter import *
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import os, cv2, json, requests, urllib.request
from urllib.request import urlopen, urlretrieve


if __name__ == '__main__':

    #url = "http://cybersherpa.net"
    #link = "https://www.instagram.com/p/B6A9PpljRpW/"
    link = "https://www.instagram.com/p/B6BECbolFFd/"
    download_path = "./"

    #print(f"requests.get(): {test_requests(url).text}")
    #print(f"urlopen: {test_urlopen(link).read()}\n\n\n")

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

    print(type_name)

    # single image
    if type_name == 'GraphImage':
        # image url from display_url in base_data directory
        display_url = base_data['display_url']
        # get the file_name from the taken_at_timestamp_value from base_data dict
        file_name = base_data['taken_at_timestamp']
        # create the path
        download_p = f"{download_path}{str(file_name)}.jpg"
        if not os.path.exists(download_p):
            #download the file
            urlretrieve(display_url, download_p)
            print("download complete")
        else:
            print('file exists')
    
    # video
    elif type_name == "GraphVideo":
        video_url = base_data['video_url']
        file_name = base_data['taken_at_timestamp']
        download_p = f"{download_path}{str(file_name)}.mp4"

        if not os.path.exists(download_p):
            urlretrieve(video_url, download_p)
            print("download complete")
        else:
            print("file exists")
    
    # mixed media
    elif type_name == "GraphSidecar":
        shortcode = base_data['shortcode']
        # Sending the requeat to INSTGRAM URL with shortcode and converting the response
        # to json and storing the response in response
        response = requests.get(f"https://www.instagram.com/p/" + shortcode + "/?__a=1").json()
        post_n, i = 1, 0

        for edge in response['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']:
            file_name = response['graphql']['shortcode_media']['taken_at_timestamp']
            download_p = f"{download_path}{str(file_name)}-{post_n}"
            is_video = edge['node']['is_video']

            if not is_video:
                display_url = edge['node']['display_url']
                download_p += ".jpg"
                if not os.path.exists(download_p):
                    urlretrieve(display_url, download_p)
                    print("download complete")
                else:
                    print("file exists")
            else:
                video_url = edge['node']['video_url']
                download_p += ".mp4"
                if not os.path.exists(download_p):
                    urlretrieve(video_url, download_p)
                    print("download complete")
                else:
                    print("file exists")
            post_n += 1


    



