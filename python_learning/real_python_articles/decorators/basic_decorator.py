#!/usr/bin/env python

def null_decorator(func):
	return func

@null_decorator
def greet():
	return 'Hello!'

if __name__ == '__main__':

	print(greet())
