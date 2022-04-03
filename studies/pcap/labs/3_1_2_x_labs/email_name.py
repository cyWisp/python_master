#!/usr/bin/env python

if __name__ == '__main__':

    email = input("Email: ")
    for l in email:
        if l == "@":
            break
        print(f"{l}", end='')
    print('')
