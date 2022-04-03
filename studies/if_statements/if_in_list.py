#!/usr/bin/env python
import sys, os

def main():
	
	pizzaToppings = ['cheese', 'pepperoni', 'sausage', 'meatLovers']

	if 'cheese' in pizzaToppings:
		print("I love cheese!")

	if 'mozarella' not in pizzaToppings:
		print("We only have regaular {}, sorry...".format(pizzaToppings[0]))

if __name__=='__main__':
	main()
