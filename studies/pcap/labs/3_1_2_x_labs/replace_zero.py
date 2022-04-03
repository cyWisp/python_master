#!/usr/bin/env python

if __name__ == '__main__':

    number = input("Number: ")
    for n in number:
        if n == '0':
            print('x', end='')
            continue
        print(n, end='')
