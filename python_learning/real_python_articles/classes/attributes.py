#!/usr/bin/env python

# An Example of class and instance attributes

class Dog():

    # Class Attributes (the same for all instnaces)
    # Class Attributes:
    species = 'mammal'

    # Instance Attributes (specific to each created object)
    # Instance Attribues:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Dog's name: {self.name}")
        print(f"Dog's age: {self.age}")


if __name__ == '__main__':

    dog_1 = Dog("Sparky", 4)
    dog_1.info()
    print(f"Species: {dog_1.species}")