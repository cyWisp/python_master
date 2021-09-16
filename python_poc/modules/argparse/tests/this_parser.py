#!/usr/bin/env python
import os, sys, argparse

def main():
	
	#new parser object
	newParse = argparse.ArgumentParser()

	#add arguments
	newParse.add_argument('length', type=int, default=0, help="The length of the object")
	newParse.add_argument('width', type=int, default=0, help="The width of the object")
	
	#parse the arguments
	args = newParse.parse_args()

	area = args.length * args.width

	print("The area is {}".format(area))
	
	

if __name__ == '__main__':
	main()
