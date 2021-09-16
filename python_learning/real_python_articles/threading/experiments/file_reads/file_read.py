#!/usr/bin/env python
import logging, os, concurrent.futures
from logging import info, INFO, basicConfig

FILE_DIR = "./files"

def logger_setup():
	format = "%(process)d - %(asctime)s - %(message)s"
	date_format = "%H:%M:%S"

	basicConfig(
		format=format,
		datefmt=date_format,
		level=INFO,
		filemode='w',
		filename='./app.log'
	)

def get_files():
	files = [[f for f in files] for root, folder, files in os.walk(FILE_DIR)][0]
	return [f"{os.path.abspath(FILE_DIR)}/{f}" for f in files]

def read_file(f):
	file_name = f.split("/")[-1]
	info(f"[+] Reading file {file_name}...")
	try:
		with open(f, 'rt') as input_file:
			content = [x.strip("\n") for x in input_file.readlines()]
	except Exception as e: logging.error("[x] Error: ", exc_info=True)
	finally: input_file.close()
	return content 

def initialize():
	print("[+] Initializing...")
	logger_setup()
	return get_files()

def read_file_threads(files):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		for f in files:
			future = executor.submit(read_file, f)
			info(f"[+] Content:")
			for line in future.result():
				info(line)

if __name__ == '__main__':
	files = initialize()
	read_file_threads(files)
