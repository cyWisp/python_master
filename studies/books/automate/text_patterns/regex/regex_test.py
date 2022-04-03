#!/usr/bin/env python
import re

if __name__ == '__main__':

    phone_number_format = re.compile(r'\d{3}-\d{3}-\d{4}')
    text_string = """this is a text string to search for phone numbers. My phone number is 786-123-1212. My mom's phone number is 234-234-1212, and my dad's phone number
is 454-454-5555
"""
    phone_numbers = phone_number_format.findall(text_string)

    print("Phone numbers found: \n")
    for number in phone_numbers:
        print(number)