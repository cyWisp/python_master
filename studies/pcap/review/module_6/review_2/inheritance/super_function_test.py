#!/usr/bin/env python

class Super:
	def __init__(self, name, age, location):
		self.name = name
		self.age = age
		self.location = location

	def __str__(self):
		return (f"My name is {self.name}, I am {self.age} years old. I live in {self.location}")
	
	def print_vars(self):
		print(f"{self.name} | {self.age} | {self.location}")

class Sub(Super):
	def __init__(self, name, age, location):
		super().__init__(name, age, location)

	def print_vars(self):
		super().print_vars()

if __name__ == '__main__':

	object_1 = Sub("Rob", "34", "Florida")

	print(object_1)
	object_1.print_vars()
		
