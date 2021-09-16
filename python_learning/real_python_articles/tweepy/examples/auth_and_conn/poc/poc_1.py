#!/usr/bin/env python
from os import environ

if __name__ == '__main__':
    stuff = environ

    print(stuff['API_KEY'])
