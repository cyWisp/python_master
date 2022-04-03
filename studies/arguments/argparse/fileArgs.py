#!/usr/bin/env python
import os, sys, argparse

def main():

	newParser = argparse.ArgumentParser()
	newParser.add_argument('file', type=str, default='', help='file to parse')
	args = newParser.parse_args()

	fileContents = []

	try:
		with open(args.file, 'rb') as readFile:
			for word in readFile:
				fileContents.append(word)
	except:
		print("unable to open file...")
	finally:
		for word in fileContents:
			print(word)
					
		readFile.close()
		print('\n' + str(fileContents[0]))

	

if __name__=='__main__':
	main()
