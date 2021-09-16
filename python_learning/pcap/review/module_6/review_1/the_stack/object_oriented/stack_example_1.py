#!/usr/bin/env python

class Stack:
	def __init__(self):
		self.stack_list = list()

if __name__ == '__main__':
	stack_object = Stack()

	# Note the instance variable is accessible from outside the class
	print(len(stack_object.stack_list))
