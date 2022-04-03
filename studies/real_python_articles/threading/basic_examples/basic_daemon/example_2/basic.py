#!/usr/bin/env python
import logging, threading
from logging import info, INFO, basicConfig
from time import sleep

def thread_function(name):
	info(f"Thread {name} starting...")
	sleep(2)
	info(f"Thread {name} ending...")

def logger_setup():
	format = "%(process)d - %(asctime)s: %(message)s"
	date_format = "%H:%M:%S"

	basicConfig(
		format=format,
		datefmt=date_format,
		level=INFO,
	)

if __name__ == '__main__':
	logger_setup()

	info("Starting three threads...")
	for i in range(3):
		new_thread = threading.Thread(target=thread_function, args=(i, ))
		new_thread.start()
		new_thread.join()

	
	

