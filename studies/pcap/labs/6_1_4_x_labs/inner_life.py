#!/usr/bin/env python
class Classy:
    varia = 1
    def __init__(self):
        self.var = 2
    
    def method(self):
        pass
    def __hidden(self):
        return "this variable"

obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)

print(obj._Classy__hidden())

