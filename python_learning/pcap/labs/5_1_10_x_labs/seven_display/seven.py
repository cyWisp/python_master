#!/usr/bin/env python
from sys import exit

def read_file(path):
    try:
        with open(path, 'r+') as digits:
            nums = [d.strip("\n") for d in digits]
    except:
        print("[x] Unable to read file.")
    else:
        return nums
    finally:
        digits.close()
    
if __name__ == '__main__':

    nums = read_file('./digits.txt')
    start, end = 0, 4
    digit_list = list()
    
    for x in range(10):
        digit = list()
        for n in nums:
            digit.append(n[start:end])
        digit_list.append(digit)
        start += 4
        end += 4

    while True:
        try:
            user_number = int(input("Number: "))
        except ValueError:
            print("[!] Please enter an integer value...")
        else:
            for i in range(5):
                for x in str(user_number):
                    print(f"{digit_list[int(x)][i]}", end="")
                print()
            break




        
        
   







        


        



