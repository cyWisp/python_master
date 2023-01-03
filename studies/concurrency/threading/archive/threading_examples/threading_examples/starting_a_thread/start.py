#!/usr/bin/env python
import logging, threading, time

def thread_function(name):
	logging.info(f"[!] Thread {name}: starting")
	time.sleep(2)
	logging.info(f"[!] Thread {name} finishing")

if __name__ == '__main__':
	format = "%(process)d - %(asctime)s %(message)s"
	logging.basicConfig(
		format=format,
		datefmt="%H:%M:%S",
		level=logging.INFO,
	)

	logging.info("[!] Main	: before creating new thread")
	new_thread = threading.Thread(target=thread_function, args=(1,))
	logging.info("[!] Main	: before starting new thread")
	new_thread.start()
	logging.info("[!] Main	: waiting for the thread to finish...")
	
	# new_thread.join()
	logging.info("[+] Main	: finished")
	
