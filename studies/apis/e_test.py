#!/usr/bin/env python

#test_image = "https://static1.e621.net/data/d7/65/d765a65f0779b948ca1529e9ce8fe194.png"
# API TESTER
# API NAME: e621

# image = requests.get(
# 	test_image,
# 	headers=e_headers,
# 	auth=HTTPBasicAuth(user_name, api_key)
# )

# try:
# 	with open('./test_image.png', 'wb') as new_image:
# 		new_image.write(image.content)
# except BaseException as e: print(f"[x] Error: {e}")
# else: print("[+] Image downloaded!")

# print(f"text: {response.text}\nencoding: {response.encoding}")

import requests, json
from requests.auth import HTTPBasicAuth
from pprint import pprint
from time import sleep

USER_NAME = 'onlyFurs'
API_KEY = 'mYxBU1hHGxydrThUvhwNmdFe'
POSTS_URL = "https://e621.net/posts.json?limit=100"
PAGES_URL = "https://e621.net/posts.json?page=12"

def get_headers():
	headers = requests.utils.default_headers()
	headers.update({'User-Agent': 'onlyFurs/onlyFursBot_v1.1.4'})
	return headers

if __name__ == '__main__':

	headers = get_headers()

	# response = requests.get(
	# 	POSTS_URL,
	# 	headers=headers,
	# 	auth=HTTPBasicAuth(USER_NAME, API_KEY),
	# )

	response = requests.get(
		PAGES_URL,
		headers=headers,
		auth=HTTPBasicAuth(USER_NAME, API_KEY),
	)

	pprint(response.json())

	# for i in response.json().values():
	# 	for x in i:
	# 		if 'female' in x['tags']['general'] and 'breasts' in x['tags']['general']:
	# 			print(x['file']['url'])
			

	

		
	
	
	
