#!/usr/bin/env python
import os, sys, argparse

def main():

	parserObject = argparse.ArgumentParser()
	
	#these are positional arguments
	parserObject.add_argument("length", type=int, default=0, help="length of the object")
	parserObject.add_argument("width", type=int, default=0, help="width of the object")

	#these are optional arguments
	parserObject.add_argument('-a', '--area', type=chr, default='a', help="determine the operation")

	args = parserObject.parse_args()

	print("The legth is {}".format(str(args.length)))
	print("The width is {}".format(str(args.width)))

	if args.a:
		print(int(args.length * args.width))


if __name__ == '__main__':
	main()
