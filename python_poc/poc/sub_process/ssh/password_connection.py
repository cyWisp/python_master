#!/usr/bin/env python
from paramiko import SSHClient


if __name__ == '__main__':

	client = SSHClient()
	client.load_host_keys('/home/wisp/.ssh/known_hosts')


	client.connect(
		'hostname/ip',
		username='username',
		password='password',		
	)

	client.close()
