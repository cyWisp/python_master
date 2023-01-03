#!/usr/bin/env python
import os, sys, shutil, random, logging, threading, time

def configure_logging():
	format = "%(process)d - %(asctime)s %(message)s"
	logging.basicConfig(
		format=format,
		datefmt="%H:%M:%S",
		handlers = [
			logging.FileHandler('./app.log', 'w', 'utf-8'),
			logging.StreamHandler(),
		],
		level=logging.INFO,
	)

def create_files():
	logging.info("[+] Checking origin directory...")
	while True:
		if sentinel(): break
		if len(os.listdir("./orig")) < 3:
			name = f"./orig/{str(random.randint(1, 9999))}.txt"
			logging.info(f"[+] Creating {name}")
			with open(name, 'w') as rg_file:
				rg_file.write(f"this is a randomly generated file called {name}")
		else: 
			logging.info("[!] Directory full, sleeping...")
			time.sleep(3)

def move_files():
	while True:
		if sentinel(): break

		logging.info("[!] Checking file count...")
		if len(os.listdir("./orig")) == 3:
			logging.info("[!] max file count reached- archiving...")
			for f in os.listdir("./orig"):
				shutil.move(os.path.join(os.path.abspath("./orig"), f), os.path.join(os.path.abspath("./dest"), f))
		else:
			logging.info("[!] No files to move, sleeping")
			time.sleep(3)

def sentinel():
	if len(os.listdir("./dest")) >= 10: return True

def run():
	create_file_thread = threading.Thread(target=create_files, args=())
	move_file_thread = threading.Thread(target=move_files, args=())
	sentinel_thread = threading.Thread(target=sentinel, args=())
	
	create_file_thread.start()
	move_file_thread.start()
	sentinel_thread.start()

if __name__ == '__main__':
	configure_logging()
	run()

