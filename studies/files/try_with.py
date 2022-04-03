#!/usr/bin/env python
import time, os, sys

def load():

	os.system("clear")
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


def writeFile():

	try:
		with open('writeFile.txt', 'w') as newFile:
			fileText = input("Write: ")
			newFile.write(fileText)
	except:
		print("could not open file")
	finally:
		newFile.close()
			
	fileText = str(fileText)
	print("you wrote: {} ".format(fileText))

def readFile():

	try:
		with open('writeFile.txt', 'rb') as readFile:
			fileText = readFile.readlines()
	except:
		print("could not open file!")
	finally:
		readFile.close()
	readFile = str(readFile)
	print("file contents: {}".format(readFile))	

def printMenu():
	
	print("\t\t*--===|File Ops|===--*\n")
	print("1. Write file")
	print("2. Read file")
	print("3. Exit")

def readOrWrite():

	
	sentinel = 0
	while sentinel == 0:
		printMenu()
		choice = int(getChoice())

		if choice == 1:
			writeFile()
			input("enter to continue")	
		elif choice == 2:
			readFile()
			input("enter to continue")
		elif choice == 3:
			sys.exit()
		
def getChoice():
	choice = input("\nSelection: ")
	return choice

def main():
	
	load()
	readOrWrite()
	
	

if __name__=='__main__':
	main()
