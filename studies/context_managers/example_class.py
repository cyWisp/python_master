#!/usr/bin/env python

class Test:
	def __init__(self):
		self.name = "rob"

	def print_name(self):
		print(f"my name is {self.name}")
	def say_goodbye(self):
		print(f"goodbye {self.name}")

if __name__ == '__main__':
	new_test = Test()

	new_test.print_name()
	new_test.say_goodbye()
