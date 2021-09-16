#!/usr/bin/env python
import os, sys

def main():


	#os.getcwd() will return the CURRENT WORKING DIRECTORY

	current_dir = os.getcwd()
	current_dir = str(current_dir)
	print(current_dir)

	#os.chdir() will change the CURRENT WORKING DIRECTORY	

	os.chdir('/home/wisp')
	current_dir = os.getcwd()
	print(current_dir)


if __name__ == '__main__':
	main()
