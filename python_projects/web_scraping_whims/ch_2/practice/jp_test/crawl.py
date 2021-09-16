#!/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time, os

def main():

	html = urlopen('file:///home/wisp/dox/dev/python/web_scraping/ch_2/practice/jp_test/index.html')
	bs_obj = BeautifulSoup(html, 'lxml')

	aList = bs_obj.findAll('a', href=True)

	for a in aList:
		link = a['href']
		time.sleep(1)
		print('Now navigating to {}'.format(link))
		
		html_2 = urlopen(str(link))
		bs_obj_2 = BeautifulSoup(html_2, 'lxml')

		child_list = bs_obj_2.findAll('a', href=True)

		os.system('clear')
		print('Printing all links on page...')
		time.sleep(1)

		for child in child_list:	
			new_link = child['href']
			if new_link == '#' or new_link == '/':
				pass
			else:	
				time.sleep(1)
			
				print(new_link)



		
		

if __name__ == '__main__':
	main()
