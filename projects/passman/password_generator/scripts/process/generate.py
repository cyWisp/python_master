#!/usr/bin/env python
from random import choice, randint
import json

CHAR_PATH = "./data/symbols.json"

def get_random_char():
    with open(CHAR_PATH, "r+") as char_file:
        chars = json.load(char_file)
    return choice(chars)

def generate_password(data, m_object):
    phrase_list = [choice(x) for x in data.data.values()]
    mangled = "".join([m_object.mangle(x) for x in phrase_list])
    random_number = "".join([str(randint(0, 9)) for x in range(4)])
    random_char = get_random_char()

    return " ".join(phrase_list), "".join([mangled, random_number, random_char])











    