#!/usr/bin/env python

class Classy:
	def other(self):
		print("other")

	def method(self):
		print("method")
		self.other()

if __name__ == '__main__':
	obj = Classy()
	obj.method()
