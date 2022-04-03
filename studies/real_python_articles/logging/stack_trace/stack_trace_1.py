#!/usr/bin/env python
import logging
from logging import basicConfig, error

if __name__ == '__main__':
	format = "%(process)d:%(asctime)s: %(message)s"
	basicConfig(
		format=format,
		level=logging.ERROR,
		datefmt="%H:%M:%S",
		filemode="w",
		filename="./app.log",
	)

	a = 5
	b = 0

	try:
		c = a / b
	except Exception as e:
		error(f"Exception occurred: {e}", exc_info=True)



