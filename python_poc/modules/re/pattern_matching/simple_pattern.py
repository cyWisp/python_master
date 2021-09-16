#!/usr/bin/env python
import re, sys

if __name__ == '__main__':

    # create a regex object
    phone_number = re.compile(r'\d{3}-\d{3}-\d{4}')
    
    # the text to be searched
    text = """this is just a test file. My phone number is 786-399-3624
We are attempting to find a phone number in this file. If there isn't one,
we should see correlating output. My dad's phone number is 786-266-1060
"""

    match_object = phone_number.findall(text) #findall returns a list
    if match_object:
        print("[!] Phone number[s] found: ")
        for num in match_object:
            print(num)
    else:
        print("No match found...")
    