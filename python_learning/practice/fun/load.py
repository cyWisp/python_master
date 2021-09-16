#!/usr/bin/env python
from os import system
from time import sleep

def lazy():
	with open('./d.txt', 'r+') as dm:
		text = [x.strip('\n') for x in dm]

	while True:
		for i in text:
			print(i, end='', sep='', flush=True)
			sleep(.08)

if '__name__' == '__main__':

	lazy()
