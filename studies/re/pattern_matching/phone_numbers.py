#!/usr/bin/env python
import sys, re

def read_file(file_name):

    try:
        with open(file_name, 'r') as read_file:
            text = read_file.readlines()
    except:
        print("[!] Unable to read file...")
    finally:
        read_file.close()

    return str(text)

def is_phone_number(text):

    pattern = "r'\d{3}-\d{3}-\d{4}'"
    match = re.findall(pattern, text)
    if match:
        return True, match
    else:
        return False
    

if __name__ == '__main__':

    if len(sys.argv) is not 2:
        print("[!] Usage: {0} <file_name>".format(sys.argv[0]))
    else:
        pass

    text = read_file(sys.argv[1])
    match, match_list = is_phone_number(text)

    if match is True:
        print("Phone number found: {0}".format(match_list[0]))
    else:
        print("No phone numbers found...")
    