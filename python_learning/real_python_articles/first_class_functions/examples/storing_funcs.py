#!/usr/bin/env python

def bark(text):
	return text.upper() + "!"

if __name__ == '__main__':

	# Creating a list of functions and methods
	funcs = [bark, str.lower, str.capitalize]
	print(funcs)

	# Calling the functions in the list with a for loop
	for f in funcs:
		print(f, f("Hi There"))

	
