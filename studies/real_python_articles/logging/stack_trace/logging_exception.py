#!/usr/bin/env python
import logging
from logging import basicConfig, exception

if __name__ == '__main__':
	format = "%(process)d-%(asctime)s: %(message)s"

	basicConfig(
		format=format,
		level=logging.ERROR,
		datefmt="%H:%M:%S",
		filemode="w",
		filename="./app.log",
	)

	try:
		var = 1 / 0
	except Exception as e:
		exception(f"Exception Occurred: {e}")
