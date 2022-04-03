#!/usr/bin/env python

class Stack:
    def __init__(self):
        self.__stackList = list()
    
    def push(self, val):
        self.__stackList.append(val)
    
    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

class SumStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    
    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

if __name__ == '__main__':
    
    stackObject = SumStack()
    
    for i in range(5):
        stackObject.push(i)
    print(stackObject.get_sum())

    for i in range(5):
        print(stackObject.pop())

