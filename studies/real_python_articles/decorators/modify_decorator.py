#!/usr/bin/env python

def uppercase(func):
	def wrapper():
		modified_result = func().upper()
		return modified_result
	return wrapper

@uppercase
def greet():
	return 'Hello'

if __name__ == '__main__':

	greeting = greet()
	print(greeting)
