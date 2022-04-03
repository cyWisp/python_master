#!/usr/bin/env python

class Range:
	def __init__(self, max):
		self.__m = max
		self.__count = 0

	def __iter__(self):
		print("Start iteration...")
		return self

	def __next__(self):
		ret = self.__count
		if self.__count < self.__m:
			self.__count += 1
		else: raise StopIteration
		return ret
				

if __name__ == '__main__':
	obj = Range(10)

	for i in obj:
		print(i)
		
