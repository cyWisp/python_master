#!/usr/bin/env python

"""
The default __str__() method returns the location of the object in memory.
You can change it by defining your own method of the name, in order to provide a better
description of the desired object.
"""

class Star:
	def __init__(self, name, galaxy):
		self.name = name
		self.galaxy = galaxy

	def __str__(self):
		return f"{self.name} in {self.galaxy}"

class Planet:
	pass

if __name__ == '__main__':

	sun = Star("Sun", "Milky Way")
	print(sun)

	earth = Planet()
	print(earth)
