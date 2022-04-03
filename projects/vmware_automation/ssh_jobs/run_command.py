#!/usr/bin/env python
from paramiko import SSHClient
from os import environ

USER = environ['VM_USER'] 
PASS = environ['VM_PASS']
HOSTS = '/home/wisp/.ssh/known_hosts'

if __name__ == '__main__':

	client = SSHClient()
	client.load_host_keys(HOSTS)
	client.connect(
		'192.168.251.130',
		username=USER,
		password=PASS,
	)

	#update = f'echo {PASS} | sudo -S apt update'
	list_upgradable = 'apt list --upgradable -a'

	stdin, stdout, stderr = client.exec_command(list_upgradable)
	
	if stdout: print(stdout.read().decode("utf-8"))
	if stderr: print(stderr.read().decode("utf-8"))

	# Get return code
	print(f"\nReturn Code: {stdout.channel.recv_exit_status()}")

	# Because they are file objects, they need to be closed
	stdin.close()
	stdout.close()
	stderr.close()

	# Close the client itself
	client.close()
