#!/usr/bin/env python
from paramiko import SSHClient
import logging, getpass, asyncio, time, json

logging.basicConfig(
	format="%(process)d - %(asctime)s: %(message)s",
	datefmt="%H:%M:%S",
	level=logging.INFO,
	handlers=[
		logging.StreamHandler(),
		logging.FileHandler('./app.log', 'w', 'utf-8')
	]
)

HOSTS = "./hosts.json"
HOSTS_TARGET = "./vm_hosts.json"
KEYS = "/home/wisp/.ssh/known_hosts"
USER = input("Username: ")
PASS = getpass.getpass("Password: ")

def read_hosts():
	logging.info(f'Reading hosts file...')
	try:
		with open(HOSTS, 'r') as hosts_file:
			hosts = json.load(hosts_file)
	except Exception as e: logging.error(f"Error: {e.__class__.__name__}: {e}")
	else:
		logging.info(f"Hosts found: {hosts}")
		return hosts

def write_hosts(hosts_dict):
	logging.info(f"Writing host mappings to {HOSTS_TARGET}...")
	try:
		with open(HOSTS_TARGET, 'w') as hosts_target:
			json.dump(hosts_dict, hosts_target)
	except Exception as e: logging.error(f"Error: {e.__class__.__name__}: {e}")

async def create_ssh_connection(host):
	logging.info(f"Creating ssh connection on {host}")

	client = SSHClient()
	client.load_host_keys(KEYS)

	client.connect(
		host,
		username=USER,
		password=PASS
	)

	return client

async def run_command(host, client):
	logging.info(f"Running command on {host}...")

	get_host_name = 'hostname'
	stdin, stdout, stderr = client.exec_command(get_host_name)
	exit_code = str(stdout.channel.recv_exit_status())

	if stdout: std_out = stdout.read().decode('utf-8').replace("\n", "")
	if stderr: std_err = "Errors: " + stderr.read().decode('utf-8').replace("\n", "")

	stdin.close()
	stdout.close()
	stderr.close()
	client.close()

	logging.info(f"IP: {host}")
	logging.info(f"Host Name: {std_out}")
	logging.info(f"Errors: {std_err}")
	logging.info(f"Exit Code: {exit_code}")

	return (std_out, std_err, "Exit code: " + exit_code)

async def chain(host):
	logging.info("Starting event chain...")
	client = await create_ssh_connection(host)
	command_results = await run_command(host, client)
	return (host, command_results)

async def main(*args):
	results = await asyncio.gather(*(chain(x) for x in args))
	return results

if __name__ == '__main__':

	hosts = read_hosts()
	results = asyncio.run(main(*hosts))
	logging.info("All threads finished")
	
	host_dict = {r[1][0]: r[0] for r in results}
	write_hosts(host_dict)

		
		


