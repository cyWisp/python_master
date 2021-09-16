#!/usr/bin/env python
from sys import argv, exit

def usage(script_name=argv[0]):
    print(f"[!] Usage: {script_name} <target_string> <search_string>")
    exit(0)

def check_args(arg_list):
    if len(arg_list) != 3:
        usage()
    else:
        if arg_list[1].isalpha() and arg_list[2].isalpha():
            return arg_list[1].upper(), arg_list[2].upper()
        else:
            print("[x] Both arguments must be comprised of letters...")
            usage()

def find_string(search_string, target_string):
    result = []
    matches = [s for s in search_string if int(target_string.find(s)) != -1]
    [result.append(x) for x in matches if x not in result]
    print(result)
    




if __name__ == '__main__':

    search_string, target_string = check_args(argv)
    find_string(search_string, target_string)

