#!/usr/bin/env python
import os, sys, argparse

def main():
	
	#create a new parse object
	parser = argparse.ArgumentParser()

	#add an argument
	parser.add_argument("l", help="Length of the object")
	parser.add_argument("w", help="Width of the object")
	
	#parse the arguments
	args = parser.parse_args()
	
	#cast argument to appropriate type
	length = int(args.l)
	width = int(args.w)

	#calculate
	area = length * width
	
	
	print("The area is {}".format(str(area)))

	try:
		with open('logFile.txt', 'a+') as log_file:
			logEntry = str(area)
			log_file.write(logEntry + '\n')
	except:
		print("could not open file for writing")
	finally:
		print("Log file written...")
		log_file.close() 
	
	
	


if __name__ == '__main__':
	main()
