#!/usr/bin/env python

# Basic class-based generator

class MyNumbers:
	def __init__(self, finish):
		self.finish = finish
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if self.a <= self.finish:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration

if __name__ == '__main__':
	myclass = MyNumbers(20)
	myiter = iter(myclass)

	for x in myiter:
		print(x)
