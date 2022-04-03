#!/usr/bin/env python

class Stack():
    def __init__(self):
        self.__stackList = []
    
    def stack_length(self):
        print(len(self.__stackList))    

if __name__ == '__main__':

    stackObject = Stack()
    stackObject.stack_length()    