#!/usr/bin/env python
import os

if __name__ == '__main__':

    name = "Rob"
    age = 12

    print("This is just a test...")
    print("Hi, my name is {0}, and I am {1} years old...".format(name, str(age)))

    if age > 18:
        print("You're allowed to watch R movies")
    else:
        print("You're too young to watch this shit...")
