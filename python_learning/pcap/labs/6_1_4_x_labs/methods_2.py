#!/usr/bin/env python
class Classy():
    def other(self):
        print("other")
    def method(self):
        print("method")
        self.other()

obj = Classy()
obj.method()
