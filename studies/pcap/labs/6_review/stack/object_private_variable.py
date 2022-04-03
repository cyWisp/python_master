#!/usr/bin/env python
class Stack:
    def __init__(self):
        self.__stackList = []

    def get_stack_size(self):
        return len(self.__stackList)

if __name__ == '__main__':

    stackObject = Stack()
    print(stackObject.get_stack_size())