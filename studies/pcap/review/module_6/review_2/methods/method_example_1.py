#!/usr/bin/env python

class Classy:
	varia = 2
	def method(self):
		print(self.varia, self.var)

if __name__ == '__main__':

	obj = Classy()
	obj.var = 3
	obj.method()
