#!/usr/bin/env python
from sys import argv, exit
from imageio import imread, mimsave
from os import listdir, path, system
from functions import intro, action_messages

OPERATIONS = action_messages()

def usage():
    print("[!] Usage: {argv[0]} <file_name> <target_directory>")
    exit(0)

def check_path(file_path):
    # check if the target path exists and is not empty
    print(OPERATIONS['check_target_directory'])
    cwd = [x.split(".")[1] for x in listdir(file_path)]
    if path.exists(file_path) and cwd != "[]":
        if "jpg" in cwd or "png" in cwd:
            print(OPERATIONS['everything_ok'])
            return [f"{path.abspath(file_path)}\\{x}" for x in listdir(file_path) if x.split(".")[1] == "jpg" or x.split(".")[1] == "png"]
        else:
            print("[x] No image files found...")
            usage()

def check_file_name(file_name):
    print(OPERATIONS['check_file_name'])
    if path.exists(f"./{file_name}"):
        print("[x] Requested file name already exists...")
        while True:
            choice = input("[?] Overwrite? [y or n]: ").upper()
            if choice == "Y":
                os.remove(file_name)
                print(OPERATIONS['everything_ok'])
                return file_name
            elif choice == "N":
                print("[x] Please re-run the program with a different file name...")
                exit(0)
            else:
                print("[x] Please select either 'y' or 'n'...")
    else:
        print(OPERATIONS['everything_ok'])
        return f"./{file_name}.gif"

# file name, directory
def check_args(arg_list):
    print(OPERATIONS['check_arg_no'])
    if len(arg_list) != 3:
        usage()
    else:
        print(OPERATIONS['everything_ok'])
        file_name = check_file_name(arg_list[1])
        image_files = check_path(arg_list[2])
        return file_name, image_files

def create_gif(file_name, image_files):
    print(OPERATIONS['reading_files'])
    images = [imread(i) for i in image_files]
    print(OPERATIONS['creating_gif'])
    mimsave(file_name, images, duration=0.2)
    print(OPERATIONS['success'])

if __name__ == '__main__':
    intro()
    file_name, image_files = check_args(argv)
    create_gif(file_name, image_files)




        
