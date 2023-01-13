#!/usr/bin/env python

def deco(func):
	def wrapper_func():
		print("this is the wrapper start")
		func()
		print("this is the wrapper end")
	return wrapper_func

@deco
def normal_func():
	print("this is the normal func")

if __name__ == '__main__':
	normal_func()
