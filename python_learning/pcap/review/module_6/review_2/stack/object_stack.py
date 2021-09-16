#!/usr/bin/env python

class Stack:
	def __init__(self):
		self.__stackList = list()

	def push(self, val):
		self.__stackList.append(val)

	def pop(self):
		val = self.__stackList[-1]
		del self.__stackList[-1]
		print(val)

if __name__ == '__main__':

	new_stack = Stack()
	new_stack.push(3)
	new_stack.push(2)
	new_stack.push(1)

	new_stack.pop()
	new_stack.pop()
	new_stack.pop()
