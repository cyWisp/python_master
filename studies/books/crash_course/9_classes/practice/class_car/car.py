#!/usr/bin/env python
import os

class Car():

	def __init__(self, make, model):
		self.make = make
		self.model = model
		self.odometer = 0

	def get_make(self):
		print('The make is {}\n'.format(self.make))

	def get_model(self):
		print('The model is {}\n'.format(self.model))

	def set_odometer(self):
		self.odometer = input('What is the odometer reading: ')

	def get_odometer_reading(self):
		print('The odometer reads {} miles'.format(self.odometer))

	def new_car(self, new_make, new_model):

		self.make = new_make
		self.model = new_model
