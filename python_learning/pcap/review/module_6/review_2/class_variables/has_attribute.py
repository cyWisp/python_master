#!/usr/bin/env python

class ExampleClass:
	def __init__(self, val):
		if val % 2 != 0: self.a = 1
		else: self.b = 1

		self.b = "some attribute"

if __name__ == '__main__':

	exampleObject = ExampleClass(1)
	print(exampleObject.a)

	try:
		print(exampleObject.b)
	except AttributeError as e:
		print(f"[x] Error: {e}")

	if hasattr(exampleObject, 'b'):
		print(exampleObject.b)
	else: print("[x] exampleObject has no attribute 'b'")
