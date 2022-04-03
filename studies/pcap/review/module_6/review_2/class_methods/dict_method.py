#!/usr/bin/env python

class Classy:
	a = 0
	def __init__(self):
		self.instance_var_1 = "instance"
		self.instance_var_2 = [1, 2, 3]

	def print_dict(self):
		for key, value in self. __dict__.items():
			print(f"{key}: {value}")


if __name__ == '__main__':
	new_class = Classy()

	new_class.print_dict()

	print(hasattr(Classy, 'a'))
	print(hasattr(new_class, 'instance_var_1'))
		
