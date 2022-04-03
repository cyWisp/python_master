#!/usr/bin/env python
import logging, threading, time

def configure_logging():
	format = "%(process)d - %(asctime)s %(message)s"
	logging.basicConfig(
		format=format,
		datefmt="%H:%M:%S",
		handlers=[
			logging.FileHandler('./app.log', 'w', 'utf-8'),
			logging.StreamHandler(),
		],
		level=logging.INFO,
	)

def thread_function(name):
	logging.info(f"[!] Thread {name} starting...")
	time.sleep(2)
	logging.info(f"[!] Thread {name} stopping...")
	

if __name__ == '__main__':
	configure_logging()

	logging.info("[!] Main")
	logging.info("[!] Starting thread functions...")

	threads = []
	
	# Non-daemonic thread example
#	for i in range(3):
#		new_thread = threading.Thread(target=thread_function, args=(i, ))
#		threads.append(new_thread)
#		new_thread.start()

	# Daemonic thread example
	for i in range(3):
		new_thread = threading.Thread(target=thread_function, args=(i, ), daemon=True)
		threads.append(new_thread)
		new_thread.start()
		new_thread.join()	# wait for the thread to finish
							# before exiting the program


	logging.info("[+] Main exiting...")

