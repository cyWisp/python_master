#!/usr/bin/env python

if __name__ == '__main__':

	income = float(input("Income: "))
	low_bracket = (income * .18) - 556.02
	high_bracket = 14839.02 + ((income - 85528.00) * .32)
	
	tax = 0

	if tax < 0 or income < 0:
		tax = 0
	else:
		if income <= 85528.00:
			tax = low_bracket
		elif income > 85528.00:
			tax = high_bracket

	tax = round(tax, 2)

	print(f"Tax: {tax} thalers")

