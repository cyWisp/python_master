#!/usr/bin/env python
import logging
from logging import debug

def logging_setup():
	format = "%(process)d - %(asctime)s - %(message)s"
	logging.basicConfig(
		level=logging.DEBUG,	
		format=format,
		filemode='w',
		filename='app.log',
		datefmt="%H%M%S",
	)

if __name__ == '__main__':
	logging_setup()
	module_name = __name__
	author_name = "Rob"

	debug("This is an opening debug message")
	debug(f"Programmer: {author_name} | Module: {module_name}")
