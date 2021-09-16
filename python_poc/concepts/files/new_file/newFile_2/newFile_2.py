#!/usr/bin/env python
import sys

def main():

	fileName = input("File Name: ")
	content = input("Content: ")

	fileName = str(fileName) + ".txt"

	try:

		with open(fileName, 'w') as newFile:
			newFile.write(content)
	except: 
		print("could not open file")
	finally:
		newFile.close()
		print("New file created and written...")


if __name__=='__main__':
	main()
