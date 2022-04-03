#!/usr/bin/env python
import sys, os

class Bike():

	def __init__(self, make, model):
		
		self.make = make
		self.model = model
		self.dateSold = ""

	def displayInfo(self):
		
		print("This bike is a " + str(self.make) + " " + str(self.model))

	def enterDateSold(dSold):
	
		dSold = input("Enter date sold: ")
		return str(dSold)
