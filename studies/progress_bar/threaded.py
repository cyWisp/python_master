#!/usr/bin/env python
import threading, time, progressbar, os, sys


#this doesn't work the way i want it to...

def load():

	loadString = 'Now Loading!!!!'
	length = len(loadString)

	for iteration in range(0, 3):
		for index, character in enumerate(loadString):
			if index == (length -1):
				print(character)
				os.system('clear')
				time.sleep(.08)
			else:
				print(character, sep='', end='', flush=True)
				time.sleep(.08)

def loadBar():
 
	bar = progressbar.ProgressBar()
	for i in bar(range(100)):
		time.sleep(0.02)


def main():

	os.system('clear')
	time.sleep(1)
	
	thread_1 = threading.Thread(target=load)
	thread_1.start()

	print('\n\n')

	thread_2 = threading.Thread(target=loadBar)
	thread_2.start()	

if __name__=='__main__':
	main()
