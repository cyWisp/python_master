#!/usr/bin/env python
import requests, concurrent.futures
from bs4 import BeautifulSoup

URLS = [
    "http://cybersherpa.net",
    "https://amazon.com",
    "https://biblegateway.com",
    "https://instagram.com"
]

def get_html(url): return requests.get(url).text
def get_links(html): return [x['href'] for x in BeautifulSoup(html, 'html.parser').findAll('a', href=True) if "https" in x['href']]
def get_site_data(url): return get_links(get_html(url))

if __name__ == '__main__':
    data = dict()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for u in URLS:
            name = u.split("/")[-1].split(".")[0]
            future = executor.submit(get_site_data, u) 
            data[name] = future.result()

    for k, v in data.items():
        print(f"site: {k}")
        for i in v:
            print(i)
        print()
