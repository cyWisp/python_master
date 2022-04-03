#!/usr/bin/env python

class Hello():
    def __init__(self, message):
        self.message = message
        self.extra = "Extra content"
    def say_hello(self):
        print(self.message)
    def show_extra(self):
        print(self.extra)

if __name__ == '__main__':

    new_hello = Hello("this is a test")

    new_hello.say_hello()
    new_hello.show_extra()
