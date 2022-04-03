#!/usr/bin/env python

class MyClass:
	pass

obj = MyClass()

obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
	for name in obj.__dict__.keys():
		if name.startswith('i'):
			val = getattr(obj, name)
			if isinstance(val, int):
				setattr(obj, name, val + 1)

if __name__ == '__main__':

	print(obj.__dict__)
	incIntsI(obj)
	print(obj.__dict__)
