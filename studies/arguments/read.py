#!/usr/bin/env python
import os, time, argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--verbose", help="Verbose Output..", action="store_true")
    parser.add_argument("file", type=str, default="", help="File to Read...")

    args = parser.parse_args()
    file_content = list()

    try:
        with open(args.file, 'r') as read_file:
            for line in read_file:
                file_content.append(line.strip('\n'))
    except:
        print("[x] Unable to open file...")
    finally:
        read_file.close()

    os.system('clear')
    time.sleep(1)

    if args.verbose:
        for line in file_content:
            print(line)
    else:
        for line in file_content[:3]:
            print(line)
        print("...")


