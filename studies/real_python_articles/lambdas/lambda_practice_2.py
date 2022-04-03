#!/usr/bin/env python

if __name__ == '__main__':
	names = ['rob', 'mark', 'sam']
	is_awesome = list(map(lambda x: x + " is awesome" if x == "rob" else x, names))

	print(is_awesome)
