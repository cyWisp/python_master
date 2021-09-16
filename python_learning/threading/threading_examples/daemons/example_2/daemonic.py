#!/usr/bin/env python
import logging, threading, time

def thread_function(name):
		logging.info(f"thread {name} starting...")
		time.sleep(2)
		logging.info(f"thread {name} finishing up...")	

def configure_logging():
	format = "%(process)d - %(asctime)s %(message)s"
	logging.basicConfig(
		format=format,
		datefmt="%H:%M:%S",
		handlers=[
			logging.StreamHandler(),
			logging.FileHandler('./app.log', 'w', 'utf-8'),
		],
		level=logging.INFO,
	)

def create_threads():
	
	threads = []
	for i in range(3):
		new_thread = threading.Thread(target=thread_function, args=(i,), daemon=True)	
		threads.append(new_thread)
		new_thread.start()

	for t in threads:
		t.join()

if __name__ == '__main__':
	configure_logging()

	logging.info("main before threads")

	create_threads()
	
	logging.info("main after threads")
