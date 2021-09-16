#!/usr/bin/env python

class Stack:
	def __init__(self):
		self.__stackList = ['rob', 'jack', 'tom']

	def show_stack(self):
		print(self.__stackList)

if __name__ == '__main__':

	stackObject = Stack()
	
	try:
		print(len(stackObject.__stackList))
	except AttributeError as a_error:
		print("Private variable!")

	try:
		stackObject.show_stack()
	except AttributeError as a_error:
		print("Private variable")
	else:
		print("Accessed from within class")

