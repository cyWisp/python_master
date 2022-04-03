#!/usr/bin/env python

if __name__ == '__main__':

    names = ["rob", "john", "bill", "sam"]
    ages = ["33", "22", "13", "24"]

    for index, name in enumerate(names):
        print(f"{name} is {ages[index]} years old...")

    names_and_ages = {a:b for a, b in zip(names, ages)}

    print("\n")
    for n, a in names_and_ages.items():
        print(f"{n} is {a} years old...")

    print("\n")
    new_dict = dict(zip(names, ages))
    for person, years in new_dict.items():
        print(f"{person} is {years} years old...")
    
