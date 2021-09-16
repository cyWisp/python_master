#!/usr/bin/env python
import time

class Tracks:
	def changedirection(self, left, on):
		print(f"tracks: {left} {on}")

class Wheels:
	def changedirection(self, left, on):
		print(f"wheels: {left} {on}")

class Vehicle:
		def __init__(self, controller):
			self.controller = controller

		def turn(self, left):
			self.controller.changedirection(left, True)
			time.sleep(0.25)
			self.controller.changedirection(left, False)

if __name__ == '__main__':
	wheeled = Vehicle(Wheels())
	tracked = Vehicle(Tracks())

	wheeled.turn(True)
	tracked.turn(False)
