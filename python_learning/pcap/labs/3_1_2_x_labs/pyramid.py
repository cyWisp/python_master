#!/usr/bin/env python

if __name__ == '__main__':

    blocks = int(input("Blocks: "))
    layer = 0

    while blocks > 0:
        if blocks > 0:
            layer += 1
            blocks -= layer
        else:
            continue
    else:
        print(layer)
