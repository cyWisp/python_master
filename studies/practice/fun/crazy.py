#!/usr/bin/env python
from os import system
from time import sleep

def load():
	system('clear')
	sleep(1)

	try:
		with open('./d.txt', 'r+') as dm:
			text = [x.strip('\n') for x in dm]
	except Exception as e: print(e)
	else:
		while True:
			for i in text:
				print(i, sep='', end='', flush=True)
				sleep(.08)
	

if __name__ == '__main__':
	load()
