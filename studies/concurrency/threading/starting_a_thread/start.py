#!/usr/bin/env python
import threading, logging, time

logging.basicConfig(
	format="%(process)d - %(asctime)s: %(message)s",
	datefmt="%H:%M:%S",
	level=logging.DEBUG,
	handlers=[logging.StreamHandler()]
)

def thread_function(name):
	logging.debug(f"Thread {name} starting...")
	time.sleep(2)
	logging.debug(f"Thread {name} ending...")

if __name__ == '__main__':
	logging.debug("In main...")
	logging.debug("Starting threads...")
	
	threads = list()

	for i in range(3):
		new_thread = threading.Thread(
			target=thread_function, 
			args=(i,), 
			daemon=True
		)
		
		threads.append(new_thread)
	
	for thread in threads:
		thread.start()
		thread.join()

	logging.debug("back in main")
	logging.debug("all done")	

