#!/usr/bin/env python

def read_int(prompt, min, max):
    while True:
        try:
            num = int(input(f"{prompt} {str(min)} to {str(max)}: "))
            assert num >= min and num <= max
        except ValueError as value_error:
            print(f"[x] Error | {value_error}")
        except AssertionError as ass_error:
            print("[x] Error | the value is not within permitted range...")
        else:
            return num

if __name__ == '__main__':

    n = read_int("Enter a number from", 0, 10)
    print(f"The number is {n}")
