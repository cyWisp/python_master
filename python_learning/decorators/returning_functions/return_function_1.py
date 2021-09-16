#!/usr/bin/env python

def parent(num):
	def first_child():
		return "hi, i am rob"
	def second_child():
		return "hi, im sam"

	if num == 1:
		return first_child
	else:
		return second_child

def parent_2(num):
	def first_child_2():
		return "hi there"
	def second_child_2():
		return "hello there..."

	if num == 1:
		return first_child_2()
	else:
		return second_child_2()


if __name__ == '__main__':

	print(parent(1))
	print(parent(2))

	print(parent_2(1))
	print(parent_2(2))
