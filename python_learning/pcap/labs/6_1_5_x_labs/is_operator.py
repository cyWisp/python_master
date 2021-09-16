#!/usr/bin/env python

class SampleClass:
    def __init__(self, val):
        self.val = val

obj_1 = SampleClass(0)
obj_2 = SampleClass(2)
obj_3 = obj_1
obj_3.val += 1

print(obj_1 is obj_2)
print(obj_2 is obj_3)
print(obj_3 is obj_1)
print(obj_1.val, obj_2.val, obj_3.val)

str_1 = "Mary had a little "
str_2 = "Mary had a little lamb"
str_1 += "lamb"

print(str_1 == str_2, str_1 is str_2)