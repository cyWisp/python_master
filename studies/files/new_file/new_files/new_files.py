#!/usr/bin/env python
import time, os, sys, os.path

def main():


	fileName = input("File Name: ")
	content = input("Content: ")

	fileName = str(fileName) + ".txt"

	try:
		with open(fileName, 'w') as newFile:
			newFile.write(str(content))
	except:
		print("file could not be opened")
	finally:
		newFile.close()
		print("File has been written...")

if __name__ == '__main__':
	main()
