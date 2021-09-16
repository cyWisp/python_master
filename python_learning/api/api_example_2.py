#!/usr/bin/env python
import requests, json

if __name__ == '__main__':

	url = "http://api.open-notify.org/iss-pass.json"
	query = {'lat': '45', 'lon':'180'}

	response = requests.get(url, params=query)

	print(response.json())

	for k, v in response.json().items():
		print(f"{k}: {v}")
	
