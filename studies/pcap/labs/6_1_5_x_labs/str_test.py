#!/usr/bin/env python

class Test:
    def __init__(self):
        self.str_var = "hello"
    def __str__(self):
        return "this is my class"


new_test = Test()
print(new_test)
print(new_test.str_var)