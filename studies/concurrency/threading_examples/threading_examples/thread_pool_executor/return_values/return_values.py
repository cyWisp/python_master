#!/usr/bin/env python
import  concurrent.futures
import logging, time

NAMES = [
	'rob',
	'christy',
	'alex',
	'martha',
]

def configure_logging():
	format = "%(process)d - %(asctime)s %(message)s"
	logging.basicConfig(
		format = format,
		datefmt = "%H:%M:%S",
		handlers = [
			logging.StreamHandler(),
			logging.FileHandler('./app.log', 'w', 'utf-8'),
		],
		level = logging.INFO,
	)

def thread_function(name):
	return f"Hi there, {name}"

if __name__ == '__main__':
	configure_logging()

	with concurrent.futures.ProcessPoolExecutor as executor:
		for name, greeting in zip(NAMES, executor.map(thread_function, NAMES)):
			logging.info(f"{name} | {greeting}")


