#!/usr/bin/env python

if __name__ == '__main__':

	data = bytearray(10)

	for i in range(len(data)):
		data[i] = 10 - i

	for b in data:
		print(hex(b))
