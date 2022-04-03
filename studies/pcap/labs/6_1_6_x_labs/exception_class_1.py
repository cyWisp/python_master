#!/usr/bin/env python

try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())