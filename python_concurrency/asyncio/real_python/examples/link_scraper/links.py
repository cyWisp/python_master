#!/usr/bin/env python
import requests
import asyncio
import time
from bs4 import BeautifulSoup

SITES = [
    "https://www.kcm.org/read/faith-to-faith",
    "http://cybersherpa.net",
    "https://example.com/",
    "https://ipchicken.com/"
]

async def get_response(url):
	return requests.get(url)

async def find_links(site):
	try:
		response = await get_response(site)
	except Exception as e:
		print(f'Request failed-\n{e}')
		return

	try:
		return [l['href'] for l in BeautifulSoup(response.content, 'html.parser').findAll('a', href=True)]
	except Exception as e:
		print(f'Could not get links-\n{e}')
		return

async def main(*args):
	links = await asyncio.gather(*(find_links(x) for x in args))
	return links

if __name__ == '__main__':
	start = time.perf_counter()
	site_links = asyncio.run(main(*SITES))
	for s in site_links:
		print(s)
		print()

	end = time.perf_counter() - start

	print(f'Execution of {__file__} took {end:0.2f} seconds...')

	
