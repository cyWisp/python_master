#!/usr/bin/env python

class ContextManager():
	def __init__(self):
		print("init method called")

	def __enter__(self):
		print("enter method called")

	def __exit__(self, exc_type, exc_value, exc_traceback):
		print("exit method called")

if __name__ == '__main__':
	with ContextManager() as manager:
		print("with statement block")


