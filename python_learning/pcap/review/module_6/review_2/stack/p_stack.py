#!/usr/bin/env python

STACK = []

def push(val):
	STACK.append(val)

def pop():
	val = STACK[-1]
	del STACK[-1]
	return val

if __name__ == '__main__':
	push(3)
	push(2)
	push(1)

	print(pop())
	print(pop())
	print(pop())
		
