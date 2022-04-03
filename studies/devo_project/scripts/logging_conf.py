#!/usr/bin/env python
import logging
from logging import info, INFO, basicConfig, FileHandler
from datetime import datetime

def configure_logging():
	format = "%(process)d - %(asctime)s: %(message)s"
	LOG_FILE_PATH = f'./{str(datetime.today()).replace(" ", "_").split(".")[0]}.log'

	basicConfig(
		format=format,
		datefmt="%H:%M:%S",
		level=INFO,
		handlers=[FileHandler(LOG_FILE_PATH, 'w', 'utf-8')]
	)

if __name__ == '__main__':
	configure_logging()

	info("this is just a test...")
