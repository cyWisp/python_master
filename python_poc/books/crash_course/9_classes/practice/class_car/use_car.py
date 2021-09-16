#!/usr/bin/env python
import os, car

def main():

	my_car = car.Car('ford', 'escort')
	my_car.get_make()
	my_car.get_model()

	new_car_make = input('New make: ')
	new_car_model = input('New model: ')

	my_car.new_car(new_car_make, new_car_model)
	print('New information:\n ')
	my_car.get_make()
	my_car.get_model()

	my_car.set_odometer()
	my_car.get_odometer_reading()


if __name__ == '__main__':
	main()
