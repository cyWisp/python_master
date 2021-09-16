#!/usr/bin/env python

if __name__ == '__main__':

    c0 = int(input("Number: "))
    steps = 0

    while c0 != 1:
        if (c0 % 2) == 0:
            c0 = c0 / 2
            print(c0)
            steps += 1
        else:
            c0 = (3 * c0) + 1
            print(c0)
            steps += 1

    print(f"steps: {steps}")

