#!/usr/bin/env python
import concurrent.futures, logging
from logging import info, INFO, basicConfig
from time import sleep

def logger_setup():
	format = "%(process)d - %(asctime)s: %(message)s"
	date_format = "%H:%M:%S"

	basicConfig(
		level=INFO,
		format=format,
		datefmt=date_format,
	)

def thread_function(name):
	info(f"Starting {name}...")
	sleep(1)
	info(f"Ending {name}...")

if __name__ == '__main__':

	logger_setup()

	# Conventional method
#	executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
#	executor.map(thread_function, range(5))

	threads = ['thread_1', 'thread_2', 'thread_3']

	# Using a context manager
	with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
		executor.map(thread_function, threads)


