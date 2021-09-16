#!/usr/bin/env python
from package_1 import mod_1

@mod_1.log_deco
def get_struct(struct):
	print('running')
	return struct

if __name__ == '__main__':
	test_dict = {
		'rob': 'awesome',
		'christy': 'more awesome',
		'alex': 'most awesome'
	}

	test_list = [
		'one',
		'two',
		'three'
	]

	test_nested_dict = {
		'first_item_dict': {
			'first_nested_key': 'first_nested_value',
			'second_nested_key': 'second_nested_value',
			'third_nested_key': 'third_nested_value',
		},
		'second_item_list':	[
			'first_nested_list_item',
			'second_nested_list_item',
			'third_nested_list_item'
		],
		'third_item_str': 'just a string',
		'fourth_item_int': 23
	}

	get_struct(test_dict)
	get_struct(test_list)
	get_struct(test_nested_dict)
