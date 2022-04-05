#!/usr/bin/env python
import time, os, sys

class Car():

	""" a simple attempt at representing a car  """

	def __init__(self, make, model, year):

		#Initializing attributes to describe a car
		
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		
		#return a neatly formatted descriptive name
		
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
	
		#print a statement showing the car's mileage
	
		print("This car has {} miles on it...".format(str(self.odometer_reading)))

	def update_odometer(self, mileage):

		#set the odometer reading to the given value
		self.odometer_reading = mileage

def main():

	my_new_car = Car('audi', 'a4', '2004')

	print(my_new_car.get_descriptive_name())

	print("old odometer reading: ")
	my_new_car.odometer_reading = 1800
	my_new_car.read_odometer()

	print("new odometer reading: ")
	my_new_car.update_odometer(1300)
	my_new_car.read_odometer()

if __name__ == '__main__':

	main()
