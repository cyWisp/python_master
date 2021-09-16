#!/usr/bin/env python
from sys import argv, exit

def check_args(arg_list):
    try:
        assert len(arg_list) == 3
        assert arg_list[1] == "-d" or arg_list[1] == '-e'
    except AssertionError:
        print(f"[!] Usage: {arg_list[0]} [-d DECODE, -e ENCODE] <message>")
        exit(0)
    else:
        return arg_list[1], arg_list[2]

def encode(message):
    encoded = [ord(m) for m in message]
    return encoded

def decode(message):
    decoded = ""
    for m in range(0, len(message), 2):
        decoded += chr(int(message[m:m+2]))
    return decoded

if __name__ == '__main__':

    operation, message = check_args(argv)
    print(decode(message), end='')





