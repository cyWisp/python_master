#!/usr/bin/env python

def my_decorator(func):
	def wrapper_func():
		print("this decorator is modifying a function")
		func()
		print("this is after the func was called...")
	return wrapper_func

@my_decorator
def regular_func():
	print("this is the func thats being decorated")

if __name__ == '__main__':
	regular_func()
