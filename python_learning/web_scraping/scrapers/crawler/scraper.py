#!/usr/bin/env python
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

class Scraper():
    
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(urlopen(url).read(), 'html.parser')

    def print_formatted(self):
        return self.soup.prettify()

    def find_page_links(self):
        links = self.soup.findAll('a')
        urls = [self.url + l['href'].lstrip('.') for l in links]
        return urls
    
        



