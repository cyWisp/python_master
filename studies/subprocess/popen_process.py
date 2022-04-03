#!/usr/bin/env python
import subprocess

if __name__ == '__main__':
    
    command = subprocess.Popen(["python3", "test.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = str(command.communicate()[0].decode("utf-8").strip('\n'))

    print(output)