#!/usr/bin/env python
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from sys import argv, exit
from bs4 import BeautifulSoup

def get_args(len_args):
    if len_args is not 2:
        print(f"[!] Usage: python {argv[0]} <url> ")
        exit(0)
    else:
        return argv[1]

def get_html(url):
    try:
        raw_html = urlopen(url).read()
    except URLError as url_error:
        print(f"[x] Something went wrong! | {url_error}")
        exit(0)
    except HTTPError as http_error:
        print(f"[x] Something went wrong! | {http_error}")
        exit(0) 
    else:
        return raw_html

def get_bsObj(html):
    return BeautifulSoup(raw_html, 'html.parser')

def find_tags(bs_obj):

    try:
        print(bsObj.nothing.nothingMore)
        print(bs_obj.h1)
    except AttributeError as a_error:
        print(f"[x] Something went wrong! | {a_error}")
    else:
        pass


if __name__ == '__main__':

    # Gather arguments
    url = get_args(len(argv))

    # Get raw html using urlopen
    raw_html = get_html(url)

    # Parse the gathered html
    bsObj = get_bsObj(raw_html)
    
    find_tags(bsObj)

    # Pull elements
    h1_tags = bsObj.h1
    links = bsObj.a

    # Print parsed html
    #print(f"{bsObj}")
    
    # Print h1 tags
    #print(f"{h1_tags}")
    #print(f"{links}")



