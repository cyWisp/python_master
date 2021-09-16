#!/usr/bin/env python
import asyncio, time, logging, requests
from bs4 import BeautifulSoup
from sys import exit

URLS = [
	"http://cybersherpa.net",
	"https://example.com",
	"http://paddlehq.fun"
]

logging.basicConfig(
	format="%(process)d - %(asctime)s: %(message)s",
	datefmt="%H:%M:%S",
	level=logging.DEBUG,
	handlers=[logging.StreamHandler()]
)

async def get_links(url):
	logging.debug(f"Requesting: {url}")
	try:
		response = requests.get(url)
	except Exception:
		await asyncio.sleep(1)
		return (url, response.status_code)

	await asyncio.sleep(1)
	links = [x['href'] for x in BeautifulSoup(response.text, 'html.parser').findAll('a', href=True)]
	return (url, links)

async def main(*args):
	links = await asyncio.gather(*(get_links(url) for url in args))
	return links

def convert_links(links):
	return {l[0]: l[1] for l in links}
	
def print_links(link_dict):
	for url, link_list in link_dict.items():
		logging.debug(f"{url}: {link_list}")

if __name__ == '__main__':
	logging.debug("Starting performance counter...")
	start = time.perf_counter()
	
	links = asyncio.run(main(*URLS))

	link_dict = convert_links(links)
	print_links(link_dict)
	end = time.perf_counter() - start

	
