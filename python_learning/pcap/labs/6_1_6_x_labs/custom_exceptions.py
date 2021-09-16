#!/usr/bin/env python

class MyZeroDivisionError(ZeroDivisionError):
    pass

def doTheDivision(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")

for mode in [False, True]:
    try:
        doTheDivision(mode)
    except ZeroDivisionError:
        print("Division by zero")

for mode in [False, True]:
    try:
        doTheDivision(mode)
    except MyZeroDivisionError:
        print("My division by zero")
    except:
        print("original division by zero")