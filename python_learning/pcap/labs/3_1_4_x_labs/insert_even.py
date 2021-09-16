#!/usr/bin/env python

if __name__ == '__main__':

    odd = ["odd" for x in range(11)]
    print(odd)

    for index, item in enumerate(odd):
        if index % 2 == 0:
            odd.insert(index, "even")

    print(odd)
