#!/usr/bin/ env python
import sys, os

class Human():

	def __init__(self, name, age):
	
		self.name = name
		self.age = age

	def talk(self):
		
		print(self.name + " is talking")
