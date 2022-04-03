#!/usr/bin/env python
from urllib.request import urlretrieve
from sys import argv, exit


if __name__ == '__main__':

	if len(argv) != 2:
		exit()

	url = argv[1]
	file_path = f"./download.{argv[1].split('.')[-1]}"

	try:	
		print(f"[+] Downloading: {url}")
		urlretrieve(url, file_path)
	except Exception as e: print(f"[x] Something went wrong! | Error: {e}")
	else: print("[+] Done!")
