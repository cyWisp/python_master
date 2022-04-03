#!/usr/bin/env python

class Super:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex

	def __str__(self):
		return self.__name__, self.__dict__

class Sub:
	def __init__(self, name, age, sex):
		super().__init__(name)

if __name__ == '__main__':

	new_class = Sub("rob", 34, "male")

	name, properties = new_class.__str__()

