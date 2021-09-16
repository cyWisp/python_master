#!/usr/bin/env python

def uppercase(func):
	def wrapper():
		original_result = func()
		modified_result = original_result.upper()
		return modified_result
	return wrapper

@uppercase
def greet():
	return "Hello!"

if __name__ == '__main__':

	print(greet())

