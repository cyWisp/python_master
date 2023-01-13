#!/usr/bin/env python
import logging, threading, requests
from bs4 import BeautifulSoup

logging.basicConfig(
	format="%(process)d - %(asctime)s: %(message)s",
	datefmt="%H:%M:%S",
	level=logging.DEBUG,
	handlers=[logging.StreamHandler()]
)

URL = "http://cybersherpa.net"

def get_html(url): return requests.get(url).text
def get_links(html):
	soup = BeautifulSoup(html, 'html.parser')
	links = soup.findAll('a', href=True)
	return [f"{URL}{x['href'].split('.')[1]}.html" for x in links]

def get_both(url):
	html = get_html(url)
	links = get_links(html)
	page_name = url.split("/")[-1]

	logging.debug(f"Page: {page_name}\n")
	logging.debug("Links: \n")
	for l in links: logging.debug(l)

if __name__ == '__main__':
	logging.debug("Gathering links...")
	html = get_html(URL)
	links = get_links(html)
	
	logging.debug(f"Parent page: {URL}")
	logging.debug("Links: \n")
	for l in links: logging.debug(l)


	logging.debug("Mapping child pages...")
	threads = list()
	for l in links:
		new_thread = threading.Thread(target=get_both, args=(l,), daemon=True)
		threads.append(new_thread)
		new_thread.start()
		
	for thread in threads:
		thread.join()

	logging.debug("Done...")

	


		


	

