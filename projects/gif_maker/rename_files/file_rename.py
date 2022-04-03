#!/usr/bin/env python
from sys import argv, exit
from os import rename, listdir

def usage():
    print(f"[!] Usage: {argv[0]} <file_name> <file_extension>")
    print("[!] This script will rename all files in the current directory with the given name and extension.")
    exit(0)

def check_files(file_type):
    print("[!] Checking file types...")
    file_types = [x.split(".")[1] for x in listdir()]
    if file_type in file_types:
        return True
    else: 
        return False

def check_args(arg_list):
    if len(arg_list) != 3:
        usage()
    else:
        if check_files(arg_list[2]):
            print("[*] File types accounted for...")
            return arg_list[1], arg_list[2]
        else:
            print("[x] Specified file type not found.")
            usage()

def rename_files(file_name, extension):
    print("[*] Enumerating files in current working directory...")
    files = listdir(".")
    for f in range(len(files)):
        if files[f].split(".")[1] == extension:
            print(f"[*] Renaming {files[f]} to {file_name}_{f}.{extension}")
            rename(f"./{files[f]}", f"./{file_name}_{f}.{extension}")
        else: pass
    print("[*] Done")
        
if __name__ == '__main__':
    file_name, extension = check_args(argv)
    rename_files(file_name, extension)
    


        
            


