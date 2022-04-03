#!/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sys import argv

if __name__ == '__main__':

    html = urlopen(argv[1]).read()
    soup = BeautifulSoup(html, 'html.parser')

    for child in soup.find("table", {"id":"giftList"}).children:
        print(child)
