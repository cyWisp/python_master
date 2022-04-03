#!/usr/bin/env python
import os

class Dog:

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def bark(self):
        print('Bark!')

    def info(self):

        print("The dog's name is {0}".format(self.name))
        print("The dog's age is {0}".format(self.age))

if __name__ == '__main__':

    new_dog = Dog('johnn boy', 13)
    new_dog.bark()
    new_dog.info()
