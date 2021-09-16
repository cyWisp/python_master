#!/usr/bin/env python
import socket

HOST = "127.0.0.1"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()

    connection, address = sock.accept()
    
    with connection:
        print(f"Connected by {address}")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)