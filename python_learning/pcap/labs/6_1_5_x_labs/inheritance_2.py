#!/usr/bin/env python
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    
    def __str__(self):
        return f"{self.name} in {self.galaxy}"

sun = Star("Sun", "Milky Way")
print(sun)