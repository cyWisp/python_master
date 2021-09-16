#!/usr/bin/env python

def yell(text):
	return text.upper() + "!"

if __name__ == '__main__':

	# yell("Get over here")
	bark = yell
	del yell

	# functions can be stored in data structures
	functions = [bark, str.lower, str.capitalize]

	# printing the contents of the list
	# print(functions)

	# accessing the function objects stored inside the list works like it would
	# with any other type of object
	for f in functions:
		print(f, f('hey there'))
	
