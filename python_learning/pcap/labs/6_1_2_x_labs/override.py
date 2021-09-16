#!/usr/bin/env python
class Stack:
    def __init__(self):
        self.__stackList = []
    
    def push(self, val):
        self.__stackList.append(val)
    
    def pop(self, val):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val
    
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def print_sum(self):
        print(self.__sum)

a_stack = AddingStack()
a_stack.push(3)
a_stack.print_sum()


