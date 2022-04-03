#!/usr/bin/env python
import re, sys

if __name__ == '__main__':

    ip = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
    text = """This is just a test. Looking to see if we can find an ip address.
Here's one 192.168.22.211. Here's another one 10.0.0.1
"""
    matches = ip.search(text)
    all_matches = ip.findall(text)

    if matches:
        print("Using search: IP found: {0}".format(matches.group()))
        print("\nUsing findall: \n")
        for match in all_matches:
            print("[!] IP found: {0}".format(match))
    else:
        print("No matches found...")
