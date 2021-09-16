#!/usr/bin/env python

if __name__ == '__main__':

    names = ['rob', 'ben', 'john']

    try:
        print(f"{names[3]}")
    except IndexError as index_error:
        print(f"[x] Error | {index_error}")
