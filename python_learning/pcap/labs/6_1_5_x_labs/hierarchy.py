#!/usr/bin/env python
import time

class TrackedVehicle:
    def controltrack(left, stop):
        pass
    def turn(left):
        controltrack(left, True)
        time.sleep(0.25)
        controltrack(left, False)

class WheeledVehicle:
    def turnfrontwheels(left, on):
        pass
    def turn(left):
        turnfrontwheels(left, True)
        time.sleep(0.25)
        turnfrontwheel(left, False)

