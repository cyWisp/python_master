#!/usr/bin/env python
import logging, asyncio, requests, time
from bs4 import BeautifulSoup
from sys import exit

URLS = [
	'http://cybersherpa.net',
	'https://example.com',
	'http://paddlehq.fun'
]

logging.basicConfig(
	format="%(process)d - %(asctime)s: %(message)s",
	datefmt="%H:%M:%S",
	level=logging.DEBUG,
	handlers=[logging.StreamHandler()]
)

async def get_html(url):
	logging.debug(f"Calling get_html({url})...")
	response = requests.get(url)
	
	logging.debug(f"get_html({url}) sleeping...")
	await asyncio.sleep(1)
	return response.status_code, response.content

async def find_links(url, status_code, html):
	logging.debug(f"Calling find_links() for {url}")
	if status_code != 200:
		return (url, status_code,  None)

	logging.debug(f"find_links() for {url} sleeping...")
	await asyncio.sleep(1)
	links = [x['href'] for x in BeautifulSoup(html, 'html.parser').findAll('a', href=True)]
	
	return (url, links)

async def chain(url):
	start = time.perf_counter()
	status_code, html = await get_html(url)
	links = await find_links(url, status_code, html)
	end = time.perf_counter() - start
	
	logging.debug(f"Process for {url} took {end:0.2f} seconds...")
	return links	

async def main(*args):
	links = await asyncio.gather(*(chain(n) for n in args))
	return links
	
if __name__ == '__main__':
	args = URLS
	start = time.perf_counter()

	links = asyncio.run(main(*args))
	end = time.perf_counter() - start
	logging.debug(f"Main finished in {end:0.2f} seconds...")
	
	for l in links:
		logging.debug(f"URL: {[0]} | Links: {l[1]}")	
