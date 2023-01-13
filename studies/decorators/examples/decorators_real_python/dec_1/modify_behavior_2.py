#!/usr/bin/env python

def make_upper(func):
	def yell(t):
		original_output = func(t)
		modified_output = original_output.upper()
		return modified_output
	return yell

@make_upper
def say_hi_decorated(text):
	return text

def say_hi(text):
	return text

if __name__ == '__main__':

	print(say_hi("hello"))
	print(say_hi_decorated("hello"))

