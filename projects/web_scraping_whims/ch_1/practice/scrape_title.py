#!/usr/bin/env python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_title(url):

	try:
		html = urlopen(url)
	except HTTPError as h_error:
		print('HTTP Error: {}'.format(h_error))
		return None

	try:
		bs_obj = BeautifulSoup(html.read(), 'lxml')
		title = bs_obj.body.h1
	except AttributeError as a_error:
		print('Attribute Error: {}'.format(a_error))
		return None

	return title

def main():

	title = get_title("http://cybersherpa.net")
	
	if title == None:
		print("Title could not be found...")
	else:
		print(title)

if __name__ == '__main__':
	main()
