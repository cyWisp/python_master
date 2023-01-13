#!/usr/bin/env python

def upper_case(func):
	def wrapper():
		original_result = func()
		modified_result = original_result.upper()
		return modified_result
	return wrapper

@upper_case
def say_hi():
	return "hi there"

if __name__ == '__main__':

	print(say_hi())
	
