#!/usr/bin/env python

class Vehicle:
	def __init__(self, color):
		self.color = color

	def __str__(self):
		print("generic vehicle")

	def move(self):
		return "moving forward"

class Car(Vehicle):
	def __init__(self, color):
		super().__init__(color)

if __name__ == '__main__':
	new_car = Car("red")
	print(new_car.move())
