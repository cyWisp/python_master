#!/usr/bin/env python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_title(url):
	
	
	#attempt to open the given url
	#in the even that the server is down, or doesn't exist, print the error
	#as an HTTPError and return None
	try:
		html = urlopen(url)
	except HTTPError as h_error:
		print('HTTP Error: {}'.format(h_error))
		return None
	
	#attempt to read the specified html tag (in this case, an h1)
	#if the tag doesn't exist, or is unreadable, print the error as an AttributeError
	#and return None
	try:
		bsObj = BeautifulSoup(html.read(), 'lxml')
		title = bsObj.body.h1
	except AttributeError as a_error:
		print('Attribute Error: {}'.format(a_error))
		return None

	#the page and tags are valid- return the specified tag (<h1> - title)
	return title
		

def main():

	#return the title from the get_title() function on the given url
	title = get_title("http://pythonscraping.com/pages/page1.html")
	
	#if the returned value is None, print a message, otherwise print the returned value
	if title == None:
		print("Title could not be found...")
	else:
		print(title)

if __name__ == '__main__':
	main()
