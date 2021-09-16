#!/usr/bin/env python

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Child class (inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}"

class Bulldog(Dog):
    def run(self, speed):
        return f"{self.name} runs {speed}"

if __name__ == '__main__':

    # Child classes inherit attributes and
    # Behaviors from the parent class
    jim = Bulldog("Jim", 12)
    print(jim.description())

    # Child classes have specific attributes and
    # behvaviors as well
    print(jim.run('slowly'))

    # Is jim an instance of Dog()?
    print(isinstance(jim, Dog))

    # Is julie and instance of Dog?
    julie = Dog("Julie", 100)
    print(isinstance(julie, Dog))