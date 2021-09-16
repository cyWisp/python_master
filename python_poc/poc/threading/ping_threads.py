#!/usr/bin/env python
import logging, threading, time
from subprocess import Popen, PIPE
from sys import exit

HOSTS_FILE = "./hosts"

def get_file_content(file_name):
	try:
		with open(file_name, "r+") as f:
			hosts = [x.rstrip("\n") for x in f.readlines()]
	except Exception as e:
		print(f"[x] Something went wrong: {e}")
	else: return hosts
	finally: f.close()

def execute(c_list):
	cmd = Popen(
		c_list,
		stdout=PIPE,
		stderr=PIPE,
	)
	output = cmd.communicate()[0].decode("utf-8")
	error = cmd.communicate()[1].decode("utf-8").rstrip("\n")
	
	if not error:
		return output
	else:
		print(f"Error: {error}")
	
def ping_hosts(host):
	c = ["ping", "-c", "2", host]
	output = execute(c)

	if output:
		s = list(output.split("\n"))
		try:
			bytes_received = int(s[5].split(",")[1].strip(" received"))
		except IndexError: print(f"{h}: Error reading data...")

		if bytes_received == 0:
			print(f"[+] {h}: Host is down")
		else:
			print(f"[+] {h}: Host is up")

if __name__ == '__main__':

	hosts = get_file_content(HOSTS_FILE)
	processes = list()

	for h in range(len(hosts)):
		new_thread = threading.Thread(target=ping_hosts, args=(hosts[h],))
		processes.append(new_thread)
	

	


