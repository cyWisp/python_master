#!/usr/bin/env python
import socket
from sys import argv, exit

if __name__ == '__main__':

	host_name = socket.gethostbyaddr(argv[1])


	print(host_name)
