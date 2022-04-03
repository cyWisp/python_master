#!/usr/bin/env python
import sys, os, time

def write_file(file_text):

    try:
        with open("./CMakeLists.txt", "w") as new_cmake:
            for line in c_make_lists:
                new_cmake.write(line)
    except:
        print("[x] Could not open file for writing...")
    finally:
        new_cmake.close()

    print("[*] CMakeLists created!")

if __name__ == '__main__':

    if len(sys.argv) == 0 or len(sys.argv) < 3 or len(sys.argv) > 3:
        print("[!] Usage {0} <num_source_files> <project_title>".format(sys.argv[0]))
        print("[!] Exiting...")
        sys.exit(0)
    else:
        try:
            int(sys.argv[1])
        except ValueError:
            print("[!] Please provide an integer for the first argument!")
            print("[!] Exiting...")
            sys.exit(0)

    #print("arguments provided: {0}, {1}".format(sys.argv[1], sys.argv[2]))

    source_file_names = list()

    os.system("clear")
    time.sleep(1)

    print("[*] Please specify all source file names: ")
    for i in range(1, (int(sys.argv[1])) + 1):
        source_file_name = input("Source file {0}: ".format(i))
        source_file_names.append(source_file_name)

    c_make_lists = """cmake_minimum_required(VERSION 3.10.2)
project({0})
include_directories(${{PROJECT_SOURCE_DIR}})
add_executable({0} """.format(str(sys.argv[2]))

    for name in source_file_names:
        c_make_lists = c_make_lists + name + " "
    c_make_lists = c_make_lists + ")"

    write_file(c_make_lists)
    print("[*] Done...")
    

        
