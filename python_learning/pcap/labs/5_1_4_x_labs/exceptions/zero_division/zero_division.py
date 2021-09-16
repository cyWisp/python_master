#!/usr/bin/env python

if __name__ == '__main__':

    while True:
        num_1 = int(input("First number: "))
        num_2 = int(input("Second number: "))
        try:
            quotient = num_1 / num_2
        except ZeroDivisionError as zero_div:
            print(f"[x] Error | {zero_div}\n[!] Try again!")
        else:
            print(f"[*] Quotient: {quotient}")
            break
        finally:
            print("[*] Done")


    
