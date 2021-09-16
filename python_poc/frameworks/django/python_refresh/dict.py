#!/usr/bin/env python
import os

if __name__ == '__main__':

    dogs = {'fido':8, 'sally':17, 'shawn':2}

    del(dogs["shawn"])
    dogs["newbie"] = 12

    for dog, age in dogs.items():
        print("{0}:{1}".format(dog, age))
