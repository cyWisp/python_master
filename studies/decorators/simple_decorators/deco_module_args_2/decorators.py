#!/usr/bin/env python

def deco(func):
	def wrapper(*args, **kwargs):
		print("something before")
		func(*args, **kwargs)
		print("something after")
	return wrapper
