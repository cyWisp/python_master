#!/usr/bin/env python
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():

	#open the given url and store it in the html variable
	html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
	#extract the html and store it in the bsObj variable
	bsObj = BeautifulSoup(html, 'lxml')

	#create a list called 'nameList' that utilizes the 
	#findAll function to pull all the span tags
	#with the class name "green" from the html
	nameList = bsObj.findAll("span", {"class":"green"})
	
	#print the plain text within each specified span tag
	for name in nameList:
		print(name.get_text())

	

if __name__ == '__main__':
	main()
