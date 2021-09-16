#!/usr/bin/env python
import logging, threading, time
from logging import info, basicConfig, INFO

def logger_setup():
	format = "[!] %(process)d - %(asctime)s: %(message)s"
	basicConfig(
	format=format, 
	level=INFO, 
	filemode='w', 
	filename='./app.log', 
	datefmt='%H:%M:%S', 
)

def thread_function(name):
	info(f"Thread {name} start")
	time.sleep(2)
	info(f"Thread {name} end")

if __name__ == '__main__':
	logger_setup()

	info("IN MAIN")
	for i in range(3):
		# Creating a daemon thread will cause the main program not to wait for
		# its execution to finish
		new_thread = threading.Thread(target=thread_function, args=(i, ), daemon=True)
		info(f"Starting thread {i}")
		new_thread.start()
		new_thread.join()	# call .join() will cause main to wait for threads to finish
	info("Waiting for thread to finish")
	info("All threads finished...")

