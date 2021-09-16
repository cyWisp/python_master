#!/usr/bin/env python
import json

if __name__ == '__main__':
    with open("./data.json", 'r+') as read_file:
        data = json.load(read_file)

