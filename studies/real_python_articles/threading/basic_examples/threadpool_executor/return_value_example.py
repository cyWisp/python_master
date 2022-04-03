#!/usr/bin/env python
import concurrent.futures

def thread_function(name):
	print(f"Hello {name}!")
	return name

if __name__ == '__main__':
	
	names = ['rob', 'john', 'bill']
	values = list()	

	with concurrent.futures.ThreadPoolExecutor() as executor:
		for n in names:
			future = executor.submit(thread_function, n)
			values.append(future.result())

	for v in values:
		print(v)
