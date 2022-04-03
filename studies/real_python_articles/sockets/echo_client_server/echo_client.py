#!/usr/bin/env python
import socket

HOST = '127.0.0.1'
PORT = 65432

if __name__ == '__main__':
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_object:
		socket_object.connect((HOST, PORT))
		socket_object.sendall(b'Hello, world')
		data = socket_object.recv(1024)

	print(f'Received {repr(data)}')
