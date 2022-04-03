#!/usr/bin/env python
import logging

if __name__ == '__main__':
	format = "%(process)d - %(asctime)s: %(message)s"
	logging.basicConfig(
		format=format,
		datefmt="%H:%M:%S",
		level=logging.DEBUG,
		handlers=[logging.FileHandler('./logfile.log', 'w', 'utf-8')],
	)

	names = ['rob', 'ben', 'joe']

	eval("[logging.debug(x) for x in names]")
