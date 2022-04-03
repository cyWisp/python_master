#!/usr/bin/env python

class Left:
	var = "L"
	varLeft = "LL"
	def fun(self):
		return "Left"

class Right:
	var = "R"
	varRight = "RR"
	def fun(self):
		return "Right"

class Sub(Left, Right):
	pass

if __name__ == '__main__':
	obj = Sub()
	print(obj.var, obj.varLeft, obj.varRight, obj.fun())
