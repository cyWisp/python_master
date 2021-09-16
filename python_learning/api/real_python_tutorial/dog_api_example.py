#!/usr/bin/env python
import requests
from pprint import pprint

if __name__ == '__main__':

	url = "https://api.thedogapi.com/v1/breeds/1"

	response = requests.get(url)
	
	# print response headers
	print("Response headers: \n")
	pprint(response.headers)
	print("\n")

	# print request headers
	print("Request headers: \n")
	pprint(response.request.headers)

	
