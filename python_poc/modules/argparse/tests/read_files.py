#!/usr/bin/env python
import os, sys, argparse

def argParser():

	takeArgs = argparse.ArgumentParser()
	takeArgs.add_argument('file', type=str, default='', help='takes a file [example.txt]')
	args = takeArgs.parse_args()

	fileContents = []

	try:
		with open(args.file, 'rb') as readFile:
			for num in readFile:
				fileContents.append(num)
	except:
		print("unable to open file...")
	finally:
		readFile.close()

	numSum = sum(fileContents)
	print(numSum)
	

def main():

	argParser()

if __name__=='__main__':
	main()
