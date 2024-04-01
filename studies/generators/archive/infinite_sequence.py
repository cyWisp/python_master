#!/usr/bin/env python

def infinite():
    num = 0
    while True:
        yield num
        num += 1
