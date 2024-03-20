#!/usr/bin/env python
import logging, functools

logging.basicConfig(
	format='%(asctime)s: %(message)s',
	datefmt='%H:%M:%S',
	level=logging.INFO,
	handlers=[logging.StreamHandler()]
)


def log_deco(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		return func(*args, **kwargs)
	return wrapper


@log_deco
def log_struct(struct):
	if isinstance(struct, dict):
		for k, v in struct.items():
			logging.info(f'{k}: {v}')
	elif isinstance(struct, list):
		for s in struct:
			logging.info(s)
	return struct

if __name__ == '__main__':
	
	test_struct = {
		'rob': '35',
		'christy': '36',
		'Kris': '31',
		'Sam': '18',
		'John': '42'
	}
	test_list = ['one', 'two', 'three', 'four', 'five']

	log_struct(test_struct)
	log_struct(test_list)

