#!/usr/bin/env python

class Stack:
	def __init__(self):
		self.__stackList = []
	
	def print_stack_length(self):
		print(len(self.__stackList))
	
	def push(self, val):
		self.__stackList.append(val)
	
if __name__ == '__main__':
	stackObject = Stack()
	stackObject.push(12)
	stackObject.push(11)

	stackObject.print_stack_length()

