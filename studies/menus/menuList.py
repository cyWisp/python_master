#!/usr/bin/env python
import time, os, sys

def load():
	
	os.system('clear')
	time.sleep(1)

	loadString = "Loading...."
	stringLength = len(loadString)
	
	for iteration in range(0,3):
		for index, character in enumerate(loadString):
			if index == (stringLength - 1):
				print(character)
				os.system('clear')
				time.sleep(.08)
			else:
				print(character, sep='', end='', flush=True)
				time.sleep(.08)	


def printMenu():
	
	print("\t*--===|List functions|===--*")
	print("1. view list")
	print("2. add to list")
	print("3. remove from list")
	print("4. exit")

def getUserInput():

	choice = input("What would you like to do? ")
	return choice

def flowControl():

	sentinel = 0
	while sentinel == 0:

		flow = getUserInput()
		
		if flow == 1:
			print("1 was selected")
			os.system('clear')
			printMenu()
		elif flow == 2:
			print("2 was selected")
			os.system('clear')
			printMenu()
		elif flow == 3:
			print("3 was selected")
			os.system('clear')
			printMenu()
		elif flow == 4:
			input("Press enter to exit...")
			sys.exit()

def main():

	load()
	printMenu()
	flowControl()

if __name__ == '__main__':
	main()
