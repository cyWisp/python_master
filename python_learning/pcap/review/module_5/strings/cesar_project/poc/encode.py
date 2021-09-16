#!/usr/bin/env python

if __name__ == '__main__':

	# 97 - 122

	message = input("message: ")

	ords = [ord(x) for x in message]
	print(ords)

	shift_value = int(input("Shift: "))

	shifted = [(y + shift_value) for y in ords]
	
	new = list()
	for c in shifted:
		if c > 122:
			diff = (c - 122) + 97
			new.append(chr(diff))
		else:
			new.append(chr(c))

	print("".join(new))
			

	

	
