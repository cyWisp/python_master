#!/usr/bin/env python

class File(object):
	def __init__(self, file_name, method):
		self.file_obj = open(file_name, method)

	def __enter__(self):
		return self.file_obj
	
	def __exit__(self, type, value, traceback):
		self.file_obj.close()

if __name__ == '__main__':

	with File('./test.txt', 'w') as test_file:
		test_file.write('HI there')
