#!/usr/bin/env python
from sys import exit, argv

from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':

    html = urlopen(argv[1]).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    links = soup.findAll('a', {'class':'nav_spacing'})

    d = [f'{argv[1]}' + l['href'].lstrip('.') for l in links]

    for l in d:
        print(f"{l} " + BeautifulSoup(urlopen(l).read(), 'html.parser').h1.get_text())
