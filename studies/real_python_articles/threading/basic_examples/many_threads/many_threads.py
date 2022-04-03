#!/usr/bin/env python
import logging, threading, time
from logging import info, INFO, basicConfig

def logger_setup():
	format = "%(process)d - %(asctime)s: %(message)s"
	date_format = "%H:%M:%S"
	basicConfig(
		format=format,
		level=INFO,
		filemode='w',
		filename='./app.log',
		datefmt=date_format,	
	)

def thread_function(name):
	info(f"starting {name}")
	time.sleep(1)
	info(f"ending {name}")

if __name__ == '__main__':
	logger_setup()

	threads = list()
	for t in range(3):
		new_thread = threading.Thread(target=thread_function, args=(t,))
		threads.append(new_thread)
		new_thread.start()

	for index, thread in enumerate(threads):
		info(f"MAIN - before joining thread {index}")
		thread.join()
		info(f"MAIN - thread {index} done...")
	

