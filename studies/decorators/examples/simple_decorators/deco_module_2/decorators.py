#!/usr/bin/env python

def add_stuff(func):
	def wrapper_func():
		print("just adding some stuff at the beginning")
		func()
		print("and adding some stuff at the end...")
	return wrapper_func
