#!/usr/bin/env python
import concurrent.futures
import logging, time

LOG_FILE = "./app.log"

class Logger:
	def __init__(self):
		self.format = "%(process)d - %(asctime)s %(message)s"
	def configure(self):
		logging.basicConfig(
			format=self.format,
			datefmt="%H:%M:%S",
			handlers=[
				logging.StreamHandler(),
				logging.FileHandler(LOG_FILE, 'w', 'utf-8'),
			],
			level=logging.INFO,
		)

def thread_function(name):
	logging.info(f"thread {name} starting...")
	time.sleep(2)
	logging.info(f"thread {name} ending...")

def start_threads():
	with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
		executor.map(thread_function, range(3))

if __name__ == '__main__':
	logger = Logger()
	logger.configure()

	start_threads()
