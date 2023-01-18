#!/usr/bin/env python

def the_decorator(func):
    def wrapper():
        print("this is before decorated func")
        func()
        print("this is after decorated func")
    return wrapper

def plain_func():
    print("this is just a func")

if __name__ == '__main__':
    decorated = the_decorator(plain_func)
    decorated()