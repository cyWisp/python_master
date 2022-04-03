#!/usr/bin/env python
class Stack:
    def __init__(self):
        self.__stackList = []
    
    def push(self, val):
        self.__stackList.append(val)
    
    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val
    
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

if __name__ == '__main__':
    new_stack = Stack()
    
    
    for x in range(10):
        print(x)
        new_stack.push(x)
    
    print()

    for y in range(10):
        print(new_stack.pop())
    
