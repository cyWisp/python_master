#!/usr/bin/env python
import logging, requests, asyncio, time
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

logging.basicConfig(
	format="%(process)d - %(asctime)s: %(message)s",
	datefmt="%H:%M:%S",
	level=logging.DEBUG,
	handlers=[logging.StreamHandler()]
)

URLS = [
	'http://cybersherpa.net',
	'https://example.com',
	'http://paddlehq.fun'
]

async def get_html(url):
	try:
		response = requests.get(url)
	except HTTPError as e:
		logging.error(f"Error: {e.__class__.__name__}: {e}")
	else: return response

async def get_links(url):
	logging.debug(f"Requesting: {url}")
	response = await get_html(url)
	if response.status_code != 200:
		logging.debug(f"Request for {url} failed: {response.status_code}")
		return (url, None)

	links_list = BeautifulSoup(response.content, 'html.parser').findAll('a', href=True)
	links = [x['href'] for x in links_list]
	return (url, links)
		
async def main(*args):
	links = await asyncio.gather(*(get_links(x) for x in args))
	return links

if __name__ == '__main__':
	start = time.perf_counter()
	
	links = asyncio.run(main(*URLS))

	elapsed = time.perf_counter() - start

	for l in links: print(f"{l[0]}:\n{l[1]}\n")
	logging.debug(f"{__file__} finished in {elapsed:0.2f} seconds...")
	
