#!/usr/bin/env python
import os

class Dog():

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print('{} is now sitting...'.format(self.name))

	def run(self):
		print('{} is now running...'.format(self.name))
