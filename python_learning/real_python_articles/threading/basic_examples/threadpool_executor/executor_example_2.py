#!/usr/bin/env python
import logging, concurrent.futures
from logging import INFO, info, basicConfig
from time import sleep

def logger_setup():
	format = "%(process)d - %(asctime)s: %(message)s"
	basicConfig(
		format=format,
		datefmt="%H:%M:%S",
		level=INFO,
	)

def thread_function(name):
	info(f"Thread {name} starting...")
	sleep(2)
	info(f"Thread {name} ending...")

if __name__ == '__main__':
	logger_setup()

	with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
		executor.map(thread_function, range(3))
	
	

	
