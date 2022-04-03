#!/usr/bin/env python
from sys import argv

if __name__ == '__main__':

    while True:
        try:
            var = int(input("var: "))
            if var < 0:
                raise Exception
        except Exception as e:
            print(f"Error: {e} | value must be greater than zero.")
        else:
            break
    
    print(var)
    

