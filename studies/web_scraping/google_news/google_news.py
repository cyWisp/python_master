#!/usr/bin/env python
from lxml import html
import requests

def main():

	#send 'get' request to retreive the web page
	response = requests.get('http://news.google.com')
	
	#check if the request succeeded (response code 200)
	if response.status_code == 200:
		
		#parse the html from webpage
		pagehtml = html.fromstring(response.text)

		#search for news headlines
		news = pagehtml.xpath('//h2[@class="esc-lead-article-title"] \
					/a/span[@class="titletext"]/text()')

	#print each news item in a new line
	print("\n".join(news))

if __name__=='__main__':
	main()
