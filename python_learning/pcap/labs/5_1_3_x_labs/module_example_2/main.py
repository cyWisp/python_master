#!/usr/bin/env python
from sys import path
path.insert(0, './test_parent/test/')
from module import hello_world

if __name__ == '__main__':

    hello_world()
