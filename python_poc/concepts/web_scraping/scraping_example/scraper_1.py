#!/usr/bin/env python
import time, os, requests

def main():
	
	query = input("Url: ")
	query = str(query)
	
	response = requests.get(query)
	txt = response.text

	print(txt)


if __name__ == '__main__':
	main()
