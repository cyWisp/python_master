#!/usr/bin/env python

# 1. import urlopen from urlib.request module
from urllib.request import urlopen

#2. import BeautifulSoup from bs4 library
from bs4 import BeautifulSoup

def main():

	#stores the result from the function URLOPEN to the variable html
	html = urlopen("http://pythonscraping.com/pages/page1.html")
	
	#stores the result from the BeautifulSoup function into the variable bsObj
	#taking the html.read() method and 'lxml' as parameters
	#'lxml' is explicitly referrences which parser to use and should always be specified
	bsObj = BeautifulSoup(html.read(), 'lxml')

	#print any h1 objects found within bsObj
	print(bsObj.h1)
	print(bsObj.title)
	print(bsObj.div)
	print(bsObj.p)

if __name__ == '__main__':
	main()
