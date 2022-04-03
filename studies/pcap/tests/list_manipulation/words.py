#!/usr/bin/env python

if __name__ == '__main__':

    sentences = [
        "this is a sentence",
        "this is another sentence",
        "this is the last sentence",
    ]

    words = [w.split(" ") for w in sentences]
    [print(f"{x[0]} {x[-1]}") for x in words]

