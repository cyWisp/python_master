#!/usr/bin/env python

def strong(func):
	def wrapper():
		return "<strong>" + func() + "</strong>"
	return wrapper

def emphasis(func):
	def wrapper():
		return "<em>" + func() + "</em>"
	return wrapper

@strong
@emphasis
def greet():
	return "Hi there..."

if __name__ == '__main__':

	 print(greet())
