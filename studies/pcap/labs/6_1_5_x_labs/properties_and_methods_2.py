#!/usr/bin/env python

class Level1:
    var = 100
    def fun(self):
        return 101

class Level2:
    var = 200
    def fun(self):
        return 201

class Level3(Level2):
    pass

obj = Level3()

print(obj.var, obj.fun())

