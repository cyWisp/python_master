#!/usr/bin/env python

class Stack:
	def __init__(self):
		self.__stack = list()

	def push(self, val):
		self.__stack.append(val)

	def pop(self):
		val = self.__stack[-1]
		del self.__stack[-1]
		return val

class Add_Stack:
	def __init__(self):
		Stack.__init__(self)
		self.__sum = 0

	def get_sum(self):
		return self.__sum	

	def push(self, val):
		self.__sum += val
		Stack.push(self, val)

	def pop(self):
		val = Stack.pop(self)
		self.__sum -= val
		return val

if __name__ == '__main__':
	new_stack = Add_Stack()

	for i in range(5):
		new_stack.push(i)

	print(new_stack.get_sum())

	for i in range(5):
		print(new_stack.pop())
