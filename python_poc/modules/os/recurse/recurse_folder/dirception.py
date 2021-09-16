#!/usr/bin/env python
import os, argparse

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('dir_num', type=int, default=0, help='number of directories to create')
	parser.add_argument('base_name', type=str, default='', help='Base name of dirs')
	args = parser.parse_args()

	for iteration in range(0, args.dir_num):
		dir_name = os.path.join('./','{}_{}'.format(args.base_name, str(iteration)))
		os.makedirs(dir_name)

	print('[*] Done...')

if __name__ == '__main__':
	main()
