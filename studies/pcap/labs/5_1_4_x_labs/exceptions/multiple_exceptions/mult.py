#!/usr/bin/env python

#def divide(x):
#    return 1/x

if __name__ == '__main__':

    try:
        num = int(input("num: "))
        q = 1/num
    except(ValueError, ArithmeticError) as err:
        print(f"[x] Error | {err}")
    else:
        print(f"Quotient: {q}")
