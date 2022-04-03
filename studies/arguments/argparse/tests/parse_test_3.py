#!/usr/bin/env python

import os, sys, argparse

"""
WorkFlow:

	1. create a new parser object
	2. add arguments and help dox
	3. parse arguments
	4. cast arguments to variables with appropriate type- can cast
		on initilization
	5. work
	6. write output/file
	7. end program

"""


def main():
	
	#new parser object
	argParserObject = argparse.ArgumentParser()
	
	#add arugments
	argParserObject.add_argument('l', '-l' '--length', type=int,
		default=0, help='length of the object')
	argParserObject.add_argument('w', '-w', '--width', type=int,
		default=0, help='width of the object')

	#parse arguments
	args = parser.parse_args()
	
	#work
	area = args.l * args.w

	#write output
	print("The area of the object is {}".format(area))

if __name__=='__main__':
	main()
