#!/usr/bin/env python
import logging
from logging import debug, basicConfig

if __name__ == '__main__':
	
	format = "%(process)d-%(asctime)s: %(message)s"
	basicConfig(
		level=logging.DEBUG,
		format=format,
		filemode='w',
		filename='./app.log',
		datefmt='%H:%M:%S',
	)

	count = 0
	while True:
		count += 1
		try:
			l = int(input("Length: "))
			w = int(input("Width: "))
			assert l > 0 and w > 0
		except AssertionError:
			debug(f"Values lower than zero: length: {l} | width: {w}")
		else: debug(f"Length: {l} | width: {w}")
		finally: 
			if count == 3: break

	
