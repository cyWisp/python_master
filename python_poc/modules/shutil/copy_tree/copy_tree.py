#!/usr/bin/env python
import os, shutil

def main():

	source = './base'
	target = './target/test_1'
	str_source = str(source)

	source = os.path.abspath(source)
	target = os.path.abspath(target)

	new_dir = str(target) + str_source.strip('.') 

	print('source: {}\ntarget: {}\nnew_dir: {}'.format(source, target, new_dir))
	
	shutil.copytree(source, new_dir)


	

if __name__ == '__main__':
	main()
