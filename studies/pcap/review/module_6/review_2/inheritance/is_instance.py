#!/usr/bin/env python

class Vehicle:
	pass

class LandVehicle(Vehicle):
	pass

class TrackedVehicle(LandVehicle):
	pass

if __name__ == '__main__':
	myVehicle = Vehicle()
	myLandVehicle = LandVehicle()
	myTrackedVehicle = TrackedVehicle()

	for obj in [
		myVehicle,
		myLandVehicle,
		myTrackedVehicle,
	]:
		for cls in [
			Vehicle,
			LandVehicle,
			TrackedVehicle,
		]:
			print(isinstance(obj, cls), end="\t")
		print()
