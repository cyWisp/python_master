#!/usr/bin/env python

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

for c1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for c2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(f"{c1} is a subclass of {c2}: {issubclass(c1, c2)}")