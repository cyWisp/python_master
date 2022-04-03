#!/usr/bin/env python

class Stack:
	def __init__(self):
		self.__stackList = list()

	def push(self, val):
		self.__stackList.append(val)

	def pop(self):
		val = self.__stackList[-1]
		del self.__stackList[-1]
		return val

class AddingStack(Stack):
	def __init__(self):
		Stack.__init__(self)
		self.__sum = 0

	def getSum(self):
		return self.__sum

	def push(self, val):
		Stack.push(self, val)
		self.__sum += val

	def pop(self):
		val = Stack.pop(self)
		self.__sum -= val
		return val

if __name__ == '__main__':

	stackObject = AddingStack()

	for i in range(5):
		stackObject.push(i)

	print(stackObject.getSum())

	for i in range(5):
		print(stackObject.pop())
