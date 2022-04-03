#!/usr/bin/env python

class One:
	def doit(self):
		print("doit from One")
	def doanything(self):
		self.doit()

class Two(One):
	def doit(self):
		print("doit from Two")

if __name__ == '__main__':
	one = One()
	two = Two()

	one.doanything()
	two.doanything()
