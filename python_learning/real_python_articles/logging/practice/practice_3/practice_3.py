#!/usr/bin/env python
import logging
from logging import debug

if __name__ == '__main__':
	format = "%(process)d - %(asctime)s - %(message)s"
	logging.basicConfig(
		format=format,
		level=logging.DEBUG,
		filemode='w',
		filename='app.log',
		datefmt="%H:%M:%S",
	)


	count = 0
	while True:
		try:
			count += 1
			if count > 3: break
			var = int(input("Enter: "))
			assert var > 5
		except AssertionError:
			debug(f"var was too low: {var}")
			continue
		else: debug(f"var was high enough")

