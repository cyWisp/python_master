#!/usr/bin/env python

if __name__ == '__main__':

    names = ['rob', 'dave', 'john', 'mike', 'bill']

    print(f"length: {len(names)} | contents: {names}")
    print("inserting bob")

    names.insert(0, 'bob')
    print(f"length: {len(names)} | contents: {names}")
    print("appending steve")

    names.append("steve")
    print(f"length: {len(names)} | contents: {names}")
