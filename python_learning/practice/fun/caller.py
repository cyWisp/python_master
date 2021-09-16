#!/usr/bin/env python
from subprocess import Popen, PIPE

def execute(c_list):
	command = Popen(
		c_list,
		stdout=PIPE,
		stderr=PIPE,
		shell=True,
	)

	output = command.communicate()[0].decode("utf-8")
	error = command.communicate()[1].decode("utf-8")

    #command.wait()

	return output, error

if __name__ == '__main__':

    command = [
        'python',
        '/home/wisp/Desktop/temp/fun/load.py',
    ]

    execute(command)


