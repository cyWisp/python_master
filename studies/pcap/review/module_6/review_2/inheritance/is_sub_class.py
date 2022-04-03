#!/usr/bin/env python

class Vehicle:
	pass

class LandVehicle(Vehicle):
	pass

class TrackedVehicle(LandVehicle):
	pass

if __name__=="__main__":
	for cls1 in [
		Vehicle,
		LandVehicle,
		TrackedVehicle,
	]:
		for cls2 in [
			Vehicle,
			LandVehicle,
			TrackedVehicle,
		]:
			print(issubclass(cls1, cls2), end="\t")
		print()
