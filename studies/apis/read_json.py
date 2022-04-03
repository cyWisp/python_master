#!/usr/bin/env python
import json
from pprint import pprint

if __name__ == '__main__':
    with open("./test.json", "r") as read_file:
        content = json.load(read_file)
    
    pprint(content)