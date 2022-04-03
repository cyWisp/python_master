#!/usr/bin/env python

class Level1:
	varia1 = 100
	def __init__(self):
		self.var1 = 101

	def fun1(self):
		return 102

class Level2(Level1):
	varia2 = 200
	def __init__(self):
		super().__init__()
		self.var2 = 201

	def fun2(self):
		return 202

class Level3(Level2):
	varia3 = 300
	def __init__(self):
		super().__init__()
		self.var3 = 301

	def fun3(self):
		return 302

if __name__ == '__main__':

	obj = Level3()

	print(obj.varia1, obj.var1, obj.fun1())
	print(obj.varia2, obj.var2, obj.fun2())
	print(obj.varia3, obj.var3, obj.fun3())
