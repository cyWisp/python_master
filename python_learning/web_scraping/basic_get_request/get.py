#!/usr/bin/env python
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from sys import argv, exit
from bs4 import BeautifulSoup

def validate_url(url):
	if url[:4] != "http":
		print("[!] Please provide a valid url")

def validate():
	if len(argv) != 2:
		print("[!] Please provide a valid url...")
		exit()
	else: validate_url(argv[1])

def get_request(url):
	try:
		html = urlopen(url).read()
	except (HTTPError, URLError) as e: print(f"[x] Error: {e}")
	return BeautifulSoup(html, 'html.parser').prettify()

if __name__ == '__main__':
	validate()
	print(get_request(argv[1]))
	
