#!/usr/bin/env python
if __name__ == '__main__':
    def nothing(n):
        raise ZeroDivisionError
    
    try:
        nothing(0)
    except ArithmeticError:
        print("error")
    print("done")
        
