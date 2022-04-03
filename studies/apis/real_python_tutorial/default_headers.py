#!/usr/bin/env python
import requests

if __name__ == '__main__':

	headers = requests.utils.default_headers()

	print("Default Headers: \n")
	for k, v in headers.items():
		print(f"{k}: {v}")
	print()


	print("Updateing user agent...")
	headers.update({'User-Agent': 'customUserAgent/customApp'})

	print("\nUpdated Headers: \n")
	for k, v in headers.items():
		print(f"{k}: {v}")
	print()



