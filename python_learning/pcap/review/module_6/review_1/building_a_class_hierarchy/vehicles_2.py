#!/usr/bin/env python
import time

class Vehicle:
	def changedirection(left, on):
		pass

	def turn(left):
		changedirection(left, True)
		time.sleep(0.25)
		changedirection(left, False)

class TrackedVehicle(Vehicle):
	def controltrack(left, stop):
		pass
	
	def changedirection(left, on):
		controltrack(left, on)

class WheeledVehicle(Vehicle):
	def turnfrontwheels(left, on):
		pass

	def changedirection(left, on):
		turnfrontwheels(left, on)
