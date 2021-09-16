####################################################
# This script takes two text files as arguments and 
# determines whether or not the text contained within them 
# is identical
####################################################
#!/usr/bin/env python
import time, os, argparse

def get_data(file_argument):
    
    data = ""

    try:
        with open(file_argument, 'r') as f_arg:
            data = f_arg.readlines()
    except:
        print('[x] Unable to open one or more files...')
    finally:
        f_arg.close()
        return data

def compare(f_1, f_2):
    
    result = ""

    if f_1 == f_2:
        result = "Match"
        return result
    else:
        result = "Mismatch"
        return result

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('file_1', type=str, default='', help='First file Argument...')
    parser.add_argument('file_2', type=str, default='', help='Second file Argument...')
    args = parser.parse_args()

    data_1 = get_data(args.file_1)
    data_2 = get_data(args.file_2)

    res = compare(data_1, data_2)

    print(res)

if __name__ == '__main__':
    main()