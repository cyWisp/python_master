#!/usr/bin/env python
import sys

def main():

	available_toppings = ['cheese', 'pepperoni', 'mushrooms', 'sausage']
	requested_toppings = ['cheese', 'pepperoni', 'veggies']

	for topping in requested_toppings:
		
		if topping in available_toppings:

			print("Adding {}".format(str(topping)))

		else:

			print("topping not available...")

		

if __name__=='__main__':
	main()
