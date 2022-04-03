#!/usr/bin/env python

def yell(text):
	return text.upper() + "!"

def whisper(text):
	return text.lower() + "..."

if __name__ == '__main__':

	functions = [yell, whisper, str.title]

	print("functions array contents: \n{0}".format(functions))
	print("\nCalling the first function in the array: \n")
	print(functions[0]("Welcome to the machine!"))

	print("\nCalling the second function in the array: \n")
	print(functions[1]("Welcome to the Machine!"))

	print("\nCalling the third function in the array: \n")
	print(functions[2]("Welcome the machine!!"))
