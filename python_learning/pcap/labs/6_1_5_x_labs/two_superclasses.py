#!/usr/bin/env python

class Super_A:
    var_A = 10
    def fun_A(self):
        return 11

class Super_B:
    var_B = 20
    def fun_B(self):
        return 21

class Sub(Super_A, Super_B):
    pass

obj = Sub()

print(obj.var_A, obj.fun_A())
print(obj.var_B, obj.fun_B())