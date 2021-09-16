#!/usr/bin/env python

class Stack:
	def __init__(self):
		self.__stackList = []

	def push(self, val):
		self.__stackList.append(val)

	def pop(self):
		val = self.__stackList[-1]
		del self.__stackList[-1]
		return val

if __name__ == '__main__':
	stack_1, stack_2, stack_3 = Stack(), Stack(), Stack()

	stack_1.push(1)
	stack_2.push(stack_1.pop() + 1)
	stack_3.push(stack_2.pop() - 2)

	print(stack_3.pop())

