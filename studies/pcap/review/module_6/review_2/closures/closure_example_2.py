#!/usr/bin/env python

def makeclosure(par):
	loc = par
	def power(p):
		return p ** loc
	return power


if __name__ == '__main__':

	fsqr = makeclosure(2)
	fcub = makeclosure(3)

	for i in range(5):
		print(i, fsqr(i), fcub(i))

