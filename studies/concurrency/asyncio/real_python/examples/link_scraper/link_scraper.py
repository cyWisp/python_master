#!/usr/bin/env python
import asyncio
import requests
from bs4 import BeautifulSoup
import logging

SITES = [
    "https://www.kcm.org/read/faith-to-faith",
    "http://cybersherpa.net",
    "https://example.com/",
    "https://ipchicken.com/"
]

async def get_content(url):
    try:
        print(f'Requesting {url}')
        return requests.get(url)
    except Exception as e:
        logging.exception(f"Request failed for {url}\nReason: {e}")

async def extract_links(response):
    return [x['href'] for x in BeautifulSoup(response.content, 'html.parser').findAll('a', href=True)]

async def get_links(url):
    try:
        response = await get_content(url)
        if response.status_code == 200:
            links = await extract_links(response)
            return links
    except Exception as e:
        logging.exception(f'Something went wrong: {e}')

async def main():
    result = await asyncio.gather(*(get_links(i) for i in SITES))
    return result

if __name__ == '__main__':
    results = asyncio.run(main())
    for r in results:
        print(r)
        print('\n\n')



