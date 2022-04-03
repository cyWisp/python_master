#!/usr/bin/env python
from paramiko import SSHClient
from getpass import getpass

KEYS = '/home/wisp/.ssh/known_hosts'

if __name__ == '__main__':
	username = input("User: ")
	password = getpass("Password: ")
	IP = '10.0.0.4'


	client = SSHClient()
	client.load_host_keys(KEYS)

	client.connect(
		IP,
		username=username,
		password=password
	)

	get_host_name = 'hostname'

	stdin, stdout, stderr = client.exec_command(get_host_name)

	if stdout: std_out = stdout.read().decode('utf-8')
	if stderr: std_err = stderr.read().decode('utf-8')

	exit_code = stdout.channel.recv_exit_status()

	stdin.close()
	stdout.close()
	stderr.close()

	client.close()

	print(f"IP: {IP}\nCommand: {get_host_name}\nCommand Result: {std_out}\nExit Code: {exit_code}")
