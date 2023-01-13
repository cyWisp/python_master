#!/usr/bin/env python
import os, logging, threading, time

PROD = "./prod"
ARCH = "./arch"

def configure_logging():
	format = "%(process)d - %(asctime)s %(message)s"
	logging.basicConfig(
		format=format,
		datefmt="%H:%M:%S",
		handlers = [
			logging.FileHandler('./app.log', 'w', 'utf-8'),
			logging.StreamHandler()
		],
		level=logging.INFO,
	)

def create_file():
	if os.path.listdir(PROD) != []:
		logging.info("[!] dir is not empty, sleeping...")
		time.sleep(2)
		logging.info("[+] Process finished!")

def move_file():
	if len(os.listdir(PROD) == 3):
		
		

def start_threads():
	pass


if __name__ == '__main__':
	configure_logging()
	
