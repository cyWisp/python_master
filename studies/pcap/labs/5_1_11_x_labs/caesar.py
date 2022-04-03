#!/usr/bin/env python
from sys import argv, exit
import string

def create_lex():
    return [chr(x) for x in range(65, 91)]

def usage(arg_list):
    print(f"[!] Usage: {arg_list[0]} [-e ENCRYPT | -d DECRYPT] <string> ([-s SHIFT VALUE]) <integer>")

def validate(arg_list):
    if (len(arg_list) != 3) and (len(arg_list) != 5):
        usage(arg_list)
        exit(0)
    else:
        if len(arg_list) == 3:
            if arg_list[1] != "-e" and arg_list[1] != "-d":
                usage(arg_list)
                exit(0)
            else:
                return arg_list[1], arg_list[2].upper() , 2
        if len(arg_list) == 5:
            if arg_list[3] != "-s":
                usage(arg_list)
                exit(0)
            else:
                try:
                    int(arg_list[4])
                except ValueError:
                    usage(arg_list)
                    exit(0)
                else:
                    return arg_list[1], arg_list[2].upper(), int(arg_list[4])

#def check_ords(ords):


def encrypt(message, shift):
    ords = [ord(x) for x in message]
    sums = [(x + shift) for x in ords]
    diff, new_ord = 0, 0
    for s in range(len(sums)):
        if sums[s] > 90:
            diff = sums[s] - 90
            new_ord = 64 + diff
            sums[s] = new_ord
        else:
            pass

    encrypted = [chr(value) for value in sums]
    return encrypted

def decrypt(message, shift):
	ords = [ord(x) for x in message]
	diffs = [(x - shift) for x in ords]
	decrypted = [chr(x) for x in diffs]

	return decrypted

def run(op, message, shift):
    if op == "-e":
        print(f"[*] ENCRYPTED: {''.join(encrypt(message, shift))}")
    else:
        print(f"[*] DECRYPTED: {''.join(decrypt(message, shift))}")

if __name__ == '__main__':
   
	op, message, shift = validate(argv)
	run(op, message, shift)
    
    
    


    


