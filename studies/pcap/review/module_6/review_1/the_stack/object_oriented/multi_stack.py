#!/usr/bin/env python

class Stack():
	def __init__(self):
		self.__stackList = list()

	def push(self, val):
		self.__stackList.append(val)

	def pop(self):
		val = self.__stackList[-1]
		del self.__stackList[-1]
		return val

if __name__ == '__main__':
	stackObject_1 = Stack()
	stackObject_2 = Stack()

	stackObject_1.push(3)
	stackObject_2.push(stackObject_1.pop())
	
	print(stackObject_2.pop())
