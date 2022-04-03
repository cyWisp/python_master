#!/usr/bin/env python

class SuperA:
	varA = 10
	def funA(self):
		return 11

class SuperB:
	varA = 22
	varB = 20
	def funB(self):
		return 21

class Sub(SuperA, SuperB):
	pass

if __name__ == '__main__':

	obj = Sub()

	print(obj.varA, obj.funA())
	print(obj.varB, obj.funB())
