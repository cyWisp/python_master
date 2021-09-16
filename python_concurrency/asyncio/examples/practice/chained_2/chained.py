#!/usr/bin/env python
import logging, requests, asyncio, time
from bs4 import BeautifulSoup

URLS = [
	"http://cybersherpa.net",
	"http://paddlehq.fun",
	"https://example.com"
]

logging.basicConfig(
	format="%(process)d - %(asctime)s: %(message)s",
	datefmt="%H:%M:%S",
	level=logging.DEBUG,
	handlers=[logging.StreamHandler()]
)

async def get_response(url):
	logging.debug(f"Requesting {url}...")
	response = requests.get(url)
	return response

async def get_links(url, response):
	logging.debug(f"Parsing response for {url}...")
	if response.status_code != 200:
		links = None

	links = [x['href'] for x in BeautifulSoup(response.content, 'html.parser').findAll('a', href=True)]

	return url, links

async def chain(url):
	logging.debug(f"Processing {url}...")
	response = await get_response(url)
	links = await get_links(url, response)

	return (url, links)

async def main(*args):
	links = await asyncio.gather(*(chain(x) for x in args))
	return links

if __name__ == '__main__':
	start = time.perf_counter()
	logging.debug(f"Starting process {__file__}")

	links = asyncio.run(main(*URLS))

	end = time.perf_counter() - start
	logging.debug(f"{__file__} took {end:0.2f} seconds...")

	print("\nResults: ")
	for l in links: print(f"Url: {l[0]}\nLinks: {l[1]}\n")
