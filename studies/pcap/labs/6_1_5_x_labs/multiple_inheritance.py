#!/usr/bin/env python
class Level_1:
    varia_1 = 100
    def __init__(self):
        self.var_1 = 101
    def fun_1(self):
        return 102

class Level_2(Level_1):
    varia_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    def fun_2(self):
        return 202

class Level_3(Level_2):
    varia_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301
    def fun_3(self):
        return 302

obj = Level_3()

print(obj.varia_1, obj.var_1, obj.fun_1())
print(obj.varia_2, obj.var_2, obj.fun_2())
print(obj.varia_3, obj.var_3, obj.fun_3())

