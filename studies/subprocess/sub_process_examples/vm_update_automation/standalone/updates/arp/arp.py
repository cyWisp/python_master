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
	pass_word = 

	arp_scan = [
		'echo', 
		pass_word, 
		'|', 
		'sudo', 
		'-S',
		'arp-scan',
		'--interface="vmnet8"',
		'--localnet',
	]

	output, error = execute(arp_scan)

	if output: print(output)
	if error: print(error)
