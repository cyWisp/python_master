#!/usr/bin/env python
import socket

# host and port variables
HOST = '127.0.0.1'
PORT = 65432

if __name__ == '__main__':
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_object:
		socket_object.bind((HOST, PORT))
		socket_object.listen()

		connection, addr = socket_object.accept()
		print(f"connection: {type(connection)}\naddr: {type(addr)}")
		with connection:
			print(f"[+] Connection from: {addr}")
			while True:
				data = connection.recv(1024)
				if not data:
					break
				connection.sendall(data)


