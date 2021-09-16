#!/usr/bin/env python

class SampleClass:
	def __init__(self, val):
		self.val = val

if __name__ == '__main__':

	ob1 = SampleClass(0)
	ob2 = SampleClass(2)
	ob3 = ob1
	ob3.val += 1

	print(ob1 is ob2)
	print(ob2 is ob3)
	print(ob3 is ob1)
	print(ob1.val, ob2.val, ob3.val, ob1.val == ob3.val)

	str1 = "Mary had a little "
	str2 = "Mary had a little lamb"
	str1 += "lamb"

	print(str1 == str2, str1 is str2)
