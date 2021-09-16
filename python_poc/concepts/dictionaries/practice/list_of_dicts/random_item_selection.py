#!/usr/bin/env python
import random

def main():

	drink_1 = {'color':'green', 'size': 'medium', 'type':'coca-cola'}
	drink_2 = {'color':'blue', 'size': 'small', 'type':'sprite'}
	drink_3 = {'color':'red', 'size': 'large', 'type':'mountain dew'}

	drinks = [drink_1, drink_2, drink_3]
	generated_drinks = []

	for d in range(0, 10):
		random_drink = random.choice(drinks)
		generated_drinks.append(random_drink)

	for r in generated_drinks:
		print(r)

if __name__ == '__main__':
	main()
