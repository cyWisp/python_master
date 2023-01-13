#!/usr/bin/env python
import concurrent.futures, logging, time

def configure_logging():
	format = "%(process)d - %(asctime)s %(message)s"
	logging.basicConfig(
		format = format,
		datefmt = "%H:%M:%S",
		handlers = [
			logging.StreamHandler(),
			logging.FileHandler("./app.log", 'w', 'utf-8'),
		],
		level = logging.INFO,
	)

def thread_function(name):
	logging.info(f"thread {name} starting...")
	time.sleep(2)
	logging.info(f"thread {name} finishing...")

if __name__ == '__main__':
	configure_logging()
	logging.info("main before initiating threaded functions")
	
	with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
		executor.map(thread_function, range(3))

	
	
	
