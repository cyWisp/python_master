#!/usr/bin/env python
import re
from sys import argv, exit

if __name__ == '__main__':
    if not argv[1]:
        print("Please provide at least one argument")
        exit()
    else: pass

    test = argv[1]
    ip_address = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    website = re.compile(r'\w{1,40}\.\w{1,40}\.\w{1,40}')
    ip_match = ip_address.search(test)
    website_match = website.search(test)

    if ip_match:
        print(f"[+] IP Address: {ip_match.group()}")
    elif website_match:
        print(f"[+] Website: {website_match.group()}")
    else:
        print("[x] No match...")