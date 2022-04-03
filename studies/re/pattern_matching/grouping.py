#!/usr/bin/env python
import re, sys

if __name__ == '__main__':

    # create a regex object
    # regex object elements can be separated by parentheses to grab specific parts of the string
    phone_number = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    
    # the text to be searched
    text = """this is just a test file. My phone number is 786-399-3624
We are attempting to find a phone number in this file. If there isn't one,
we should see correlating output. My dad's phone number is 786-266-1060
"""

    match_object = phone_number.search(text)
    if match_object:
        print("Area Code: {0}\nNumber: {1}\nComplete Phone Number: {2}".format(match_object.group(1), match_object.group(2), match_object.group(0)))
    else:
        print("No match found...")