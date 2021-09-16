#!/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():

	url = input('URL: ')

	html = urlopen(url)
	bsObj = BeautifulSoup(html, 'lxml')

	formatted = bsObj.prettify()

	print(formatted)

	with open('site.html', 'w') as new_site:
		for line in formatted:
			new_site.write(line)
	new_site.close()

if __name__ == '__main__':
	main()
