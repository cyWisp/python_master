#!/usr/bin/env python
import requests
import json

if __name__ == '__main__':

	url = "http://api.open-notify.org/astros.json"

	response = requests.get(url)
	json_var = response.json()

	for k, v in json_var.items():
		print(k)
		if isinstance(v, list):
			for i in v:
				print(i)
		else: print(v)


	print(json_var['people'][1]['name'])
	
