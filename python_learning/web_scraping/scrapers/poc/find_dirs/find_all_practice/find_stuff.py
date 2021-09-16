#!/usr/bin/env python
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from sys import argv, exit
import os

def check_args():
    if len(argv) is not 2:
        print(f"[!] Usage: {argv[0]} <URL>")
        exit(0)
    else:
        return argv[1]

def get_raw(url):
    return urlopen(url).read()

def get_attributes(html):
    
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.findAll('div', {'class':'single_column'}, recursive=True)
    headers = soup.findAll('h1', {'class':'title'}, recursive=True)
    metas = soup.findAll('meta')

    return divs, headers, metas

if __name__ == '__main__':

    raw = get_raw(check_args())
    
    #test_1
    #print(raw)

    #divs, headers, metas = get_attributes(raw)
    print(BeautifulSoup(raw, 'http.parser').prettify())
    
