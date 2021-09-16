#!/usr/bin/env python
import concurrent.futures, logging

logging.basicConfig(
	format="%(asctime)s: %(message)s",
	datefmt="%H:%M:%S",
	level=logging.INFO,
	handlers=[logging.StreamHandler()]
)

def say_hi(name):
	logging.info(f"Starting thread {name}")
	time.sleep(2)
	logging.info(f"Ending thread {name}")

if __name__ == '__main__':
	with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
		executor.map(say_hi, range(3))
	
