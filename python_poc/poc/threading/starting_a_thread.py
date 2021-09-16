#!/usr/bin/env python
import logging, threading, time

def thread_function(name):
	logging.info(f"Thread {name}: starting")
	time.sleep(2)
	logging.info(f"Thread {name} finishing")

if __name__ == '__main__':

	format = "%(asctime)s: %(message)s"

	logging.basicConfig(
		format=format,
		level=logging.INFO,
		datefmt="%H:%M:%S"
	)

	logging.info("Main	: before creating thread")
	x = threading.Thread(target=thread_function, args=(1,))
	
	logging.info("Main	: before running thread")
	x.start()

	logging.info("Main	: wait for the thread to finish")
	# x.join()
	logging.info("Main	: all done")

