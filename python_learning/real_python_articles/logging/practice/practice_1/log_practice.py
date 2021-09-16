#!/usr/bin/env python
import logging
from logging import debug

def logging_setup():
	format = "%(process)d - %(asctime)s: %(message)s"
	logging.basicConfig(
		level=logging.DEBUG,
		format=format,
		filemode='w',
		filename='log.txt',
		datefmt="%H:%M:%S",
	)

if __name__ == '__main__':
	logging_setup()
	some_var = "rob is awesome"


	debug("this is a debug message")
	debug(f"contents of some_var: {some_var}")


