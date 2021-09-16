#!/usr/bin/env python
from requests import get
from bs4 import BeautifulSoup

def write_source(html, file_name):
	try:
		with open(file_name, 'w+') as source_file:
			source_file.write(html)
	except Exception as e:
		print(f"[x] Error: {e}")
	else:
		print(f"{file_name} written!")
	finally: source_file.close()

if __name__ == '__main__':

	html = dict()
	url = "http://cybersherpa.net"
	response = get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	html['index.html'] = response.text

	links = soup.findAll('a', href=True)
	new_links = [url + l['href'].lstrip('.') for l in links]

	for n in new_links:
		html[n.split("/")[-1]] = get(url).text
	
	for k, v in html.items():
		write_source(v, k)
		
	
	
