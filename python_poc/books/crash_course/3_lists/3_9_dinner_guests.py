#!/usr/bin/env python
if __name__ == '__main__':

    names = list()

    while True:
        person = input("Name: ")
        if person:
            names.append(person)
        else:
            break

    print("List of names: \n")

    for name in names:
        print(name)
    print("\nNumber of Dinner Guests: {}".format(len(names)))