#!/usr/bin/env python
from subprocess import Popen, PIPE
from getpass import getpass

def execute(c_list):
	command = Popen(
		c_list,
		stdout=PIPE,
		stderr=PIPE,
	)

	output = command.communicate()[0].decode("utf-8")
	error = command.communicate()[1].decode("utf-8")

	return output, error

if __name__ == '__main__':

	pw = getpass("[?] Password: ")

	commands = {
		"apt_update": ["apt", "update"],
		"u": ["uname", "-a"]
	}

	output, error = execute(commands["apt_update"])
	print(f"{output}\n{error}")

