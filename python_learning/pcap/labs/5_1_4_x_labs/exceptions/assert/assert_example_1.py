#!/usr/bin/env python

if __name__ == '__main__':

    while True:
        try:
            num = int(input("num: "))
            assert num >= 0
        except AssertionError:
            print("num cannot be negative")
        else:
            print(num)
            break

