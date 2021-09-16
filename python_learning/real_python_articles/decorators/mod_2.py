#!/usr/bin/env python

def uppercase(func):
	def wrapper():
		original = func()
		mod = original.upper() + "!"
		return mod
	return wrapper

@uppercase
def text():
	return "hi there"

def text_2():
	return "hi there"

if __name__ == '__main__':

	print("Decorated: ")
	print(text() + "\n")

	print("Undecorated: ")
	print(text_2())

