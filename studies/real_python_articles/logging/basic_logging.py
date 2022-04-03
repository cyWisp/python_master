#!/usr/bin/env python
import logging

if __name__ == '__main__':
	format = "%(asctime)s: %(message)s"
	logging.basicConfig(
		format=format, 
		level=logging.DEBUG,
		datefmt="%H:%M:%S", 
		filemode='w', 
		filename='log.txt',
	)

	logging.debug("this is a debug message")

	var = "that"

	logging.debug(f'contents of var: {var}')

	
