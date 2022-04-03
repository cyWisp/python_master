#!/usr/bin/env python
import os, sys, argparse

def main():

	newParser = argparse.ArgumentParser()

	newParser.add_argument("file", type=str, default="", help="The file to read...")
	args = newParser.parse_args()

	fileContents = []
	
	try:
		with open(args.file, "rb") as readFile:
			for character in readFile:
				fileContents.append(character)
	except:
		print("could not open file")
	finally:
		print("File contents: \n")
		for textChar in fileContents:
			print(textChar)
		readFile.close()

if __name__=='__main__':
	main()
