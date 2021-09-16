#!/usr/bin/env python
import os

def area(h, w):

    return (int(h)*int(w))

def perimeter(h, w):

    return ((int(h)*2) + (int(w)*2))

if __name__ == '__main__':

    height = input("Height: ")
    width = input("Width: ")

    per = perimeter(height, width)
    ar = area(height, width)

    print("The perimeter is {0}".format(str(per)))
    print("The area is {0}".format(str(ar)))
