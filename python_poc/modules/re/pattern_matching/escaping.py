#!/usr/bin/env python
import re, sys

if __name__ == '__main__':

    # grouping and escaping characters such as parentheses
    phone_number = re.compile(r'(\(\d{3}\))(\d{3}-\d{4})') # escaping parentheses with "\"
                                                           # each must be escaped individually
    
    text = """this is just a test file. My phone number is (786)399-3624
We are attempting to find a phone number in this file. If there isn't one,
we should see correlating output.
"""
    matches = phone_number.search(text)

    if matches:
        area_code, number = matches.groups()
        complete_number = matches.groups(0)
        print("Area Code: {0}\nNumber: {1}\nComplete Number: {2}".format(area_code, number, complete_number))
    else:
        print("No matches found...")