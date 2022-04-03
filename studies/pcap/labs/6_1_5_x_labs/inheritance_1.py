#!/usr/bin/env python

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    
sun = Star("Sun", "Milky Way")

print(sun)