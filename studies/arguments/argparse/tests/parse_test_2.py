#!/usr/bin/env python
import os, sys, argparse
from datetime import datetime

def main():
	
	#create a new parser object
	newParser = argparse.ArgumentParser()

	#add arguments and help documenation
	newParser.add_argument("l", help="the length of the object")
	newParser.add_argument("w", help="the width of the object")

	#parse the arguments
	args = newParser.parse_args()

	#cast the arguments to appropriate types
	length = int(args.l)
	width = int(args.w)

	#calculate area 
	area = length * width

	#initilize date time variable
	logTime = datetime.now()
	logTimeEntry = "Time of calculation: " + str(logTime)
	formatting = "*****************************************"

	print("The area of the given object is {}".format(str(area)))

	#record the output to a text file
	try:
		with open("newLog.txt", "a+") as log_file:
			logEntry = str(area)
			log_file.write("{} \n{} \n{} \n".format(logTimeEntry, logEntry, formatting))
	except:
		print("Could not open file for writing...")
	finally:
		print("Data saved to log")
		log_file.close()

if __name__=='__main__':
	main()
