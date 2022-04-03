#!/usr/bin/env python
import os

def main():

	currentDir = os.getcwd()
	currentDir = str(currentDir)

	print("The current working directory is {}".format(currentDir))
	createDir = input("Name of new Dir: ")
	os.makedirs(createDir)
	
	print("Navigating into newly created dir...")
	
	os.chdir(createDir)
	newCurrentDir = os.getcwd()
	print("You are now in the {} directory".format(newCurrentDir))
	

if __name__ == '__main__':
	main()
