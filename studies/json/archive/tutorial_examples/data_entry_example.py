#!/usr/bin/env python
import json

if __name__ == '__main__':

	num_employees = int(input("Number of employees: "))

	emps = dict()

	for i in range(num_employees):
		name = str(input("name: "))
		age = int(input("age: "))
		
		emps[name] = age

	emps_data = json.dumps(emps, indent=4)

	print(emps_data)
	
