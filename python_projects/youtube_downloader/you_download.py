#!/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pytube import YouTube
import argparse

if __name__ == '__main__':

   
   #Get search criteria and number of files to download
    parser = argparse.ArgumentParser()
    parser.add_argument('search', type=str, default='', help='Search String')
    parser.add_argument('num_vids', type=int, default=1, help='Number of videos...')
    args = parser.parse_args()

    #handle spaces in search string
    search_parse = args.search
    if ' ' in search_parse:
        joined_string = search_parse.replace(' ', '+')
        search_string = 'https://www.youtube.com/results?search_query=' + joined_string
    else:
        search_string = 'https://www.youtube.com/results?search_query=' + args.search

    #print search string for referrence
    print('[!] Search string: {0}'.format(search_string))

    #create html and soup objects
    page = urlopen(search_string).read()
    bs = BeautifulSoup(page, 'html.parser')

    #find all links
    videos = bs.findAll('a',{'class': 'yt-uix-tile-link'})

    video_list = []
    for video in videos:
        tmp = 'https://www.youtube.com' + video['href']
        video_list.append(tmp)

    for index, item in enumerate(video_list):

        vid = YouTube(item)
        video = vid.streams.first()
        video.download('./')
        
        if index == (args.num_vids - 1):
            break
        else:
            pass
    



    