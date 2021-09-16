#!/usr/bin/env python

stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

if __name__ == '__main__':
    push(3)
    push(2)
    push(1)

    print(pop())
    print(pop())
    print(pop())


