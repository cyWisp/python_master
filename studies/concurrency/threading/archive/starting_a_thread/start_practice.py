#!/usr/bin/env python
import threading, logging, time

logging.basicConfig(
	format="%(process)d - %(asctime)s: %(message)s",
	datefmt="%H:%M:%S",
	level=logging.DEBUG,
	handlers=[logging.StreamHandler()]
)

def thread_function(name):
	logging.debug(f"Starting {name}...")
	time.sleep(2)
	logging.debug(f"Ending {name}...")

if __name__ == '__main__':
	threads = list()
	for i in range(3):
		logging.debug(f"Main creating and starting thread {i}")
		new_thread = threading.Thread(target=thread_function, args=(i,))
		threads.append(new_thread)
		new_thread.start()

	for index, thread in enumerate(threads):
		logging.debug(f"Main before joining thread {index}")
		thread.join()
		logging.debug(f"Main thread {index} done...")
		
