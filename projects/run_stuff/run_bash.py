#!/usr/bin/env python
import subprocess, sys

if __name__ == '__main__':

    command = sys.argv[1]
    #argument = sys.argv[2]

    exec_command = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    exec_command.wait()
    output = exec_command.communicate()[0]
    errors = exec_command.communicate()[1]

    if errors:
        print(errors.decode("utf-8").strip("\n"))

    decoded_output = output.decode("utf-8").strip("\n")

    print(decoded_output)
