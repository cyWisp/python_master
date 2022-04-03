#!/usr/bin/env python
import os

class Human():

	def __init__(self, name, age):
		
		self.name = name
		self.age = age
	
	def introduction(self, greeting):
	
		print('{}, my name is {}! Nice to meet you!'.format(greeting, self.name))

	def say_age(self):

		print("My name is {}, I'm {} years old...".format(self.name, str(self.age)))
