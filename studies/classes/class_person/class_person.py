#!/usr/bin/env python
import time, os

class Person():

	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.jobs = 0

	def setJobs(self):
		self.jobs = input("How many jobs has " + self.name + " had?")

	def sit(self):
		print(self.name + " is now sitting...")

	def walk(self):
		print(self.name + " is now waking...")

	def sayMyName(self):
		print("The person's name is " + self.name + ", he is " + self.age + " years old...")

def printBanner():

	print("CLASS PRACTICE... YAY!")



