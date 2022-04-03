#!/usr/bin/env python
import re, sys

if __name__ == '__main__':

    social = re.compile(r'(\d{3})-(\d{2})-(\d{4})')
    text = """this is just some random social security number
it is 343-43-1232
"""

    mo = social.search(text)

    if mo:
        print("first group: {0}\nsecond group: {1}\n third group: {2}\nfull match: {3}".format(mo.group(1), mo.group(2), mo.group(3), mo.group(0)))