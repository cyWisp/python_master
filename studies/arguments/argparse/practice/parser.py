#!/usr/bin/env python
import os, argparse

def main():

	argument = argparse.ArgumentParser()
	argument.add_argument('--file', type=str, default='', help='File to read..')
	arg = argument.parse_args()

	lines = []

	try:
		with open(arg.file, 'r') as read_file:
			for line in read_file:
				lines.append(line.strip())
	except:
		print('File IO error...')
	finally:
		read_file.close()

	for line in lines:
		print(line)
		
		
		
	
		

if __name__ == '__main__':
	main()
