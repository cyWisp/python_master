#!/usr/bin/env python
from subprocess import call

if __name__ == '__main__':

	pwd = ""
	cmd = 'sudo arp-scan --interface=vmnet8 --localnet'

	call(cmd)
