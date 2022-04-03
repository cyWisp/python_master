#!/usr/bin/env python
from subprocess import Popen, PIPE

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

	update = ["sudo", "apt", "update"]
	list_upgradable = ["apt", "list", "--upgradable", "-a"]
	
	output, error = execute(update)
	output, error = execute(list_upgradable)

	print(f"{output}\n\n{error}")

	

	
