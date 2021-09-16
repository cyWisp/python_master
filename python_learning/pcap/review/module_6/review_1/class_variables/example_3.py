#!/usr/bin/env python

class ExampleClass:
	varia = 1
	def __init__(self, val):
		ExampleClass.varia = val

if __name__ == '__main__':

	print("ExampleClass dict: \n")
	for i, j in ExampleClass.__dict__.items():
		print(f"{i} : {j}")

	print()

	exampleObject = ExampleClass(2)

	print(ExampleClass.__dict__)
	print(exampleObject.__dict__)
		
