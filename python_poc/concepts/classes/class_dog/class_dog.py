#!/usr/bin/env python
import os, sys

class Dog():

	def __init__(self, name, age):
		
		self.name = name
		self.age = age

	def sit(self):
		
		print(self.name + " is now siting.")
		print(self.name + " is " + self.age + " years old.")

	def rollover(self):

		print(self.name + " has just rolled over.")
		
