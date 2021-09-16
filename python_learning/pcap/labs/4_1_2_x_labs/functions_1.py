#!/usr/bin/env python

def greet_person(last_name, first_name='Batman'):

	print(f"Good morning {first_name} {last_name}, how are you?")

if __name__ == '__main__':

	# Using positional arguments
	greet_person("Bill", "Gates")

	# Using keyword argument passing
	# greet_person(last_name='Williams', first_name='Johnny')

	greet_person("Doe", "John")
	greet_person("Douglas", first_name="Martin")

