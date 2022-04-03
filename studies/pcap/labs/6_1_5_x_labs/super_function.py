#!/usr/bin/env python
class Super:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"My name is {self.name}, and I am {self.age} years old..."

class Sub(Super):
    def __init__(self, name, age):
        super().__init__(name, age)

obj = Sub("Andy", "33")

print(obj)