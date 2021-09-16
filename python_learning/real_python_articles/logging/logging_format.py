#!/usr/bin/env python
import logging
from logging import debug

if __name__ == '__main__':
	format = "%(process)d: %(asctime)s: %(message)s"
	logging.basicConfig(
		format=format,
		level=logging.DEBUG,
		datefmt='%H:%M:%S',
		filemode='w',
		filename='./log.txt',
	)
	
	var = "rob"

	debug("this is another debug message")
	debug(f"the author's name is {var}")

