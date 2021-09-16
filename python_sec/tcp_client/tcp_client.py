#!/usr/bin/env python
import socket
from sys import argv, exit

PORT = 80

def usage(name = argv[0]):
    print(f"[!] Usage: {name} <URL>")
    exit()

def validate(args = argv):
    if len(args) != 2: usage()
    else: pass

def create_socket():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client

def connect_socket(client, host, port=PORT):
    client.connect((host, port))
    return client

def get_host_name(host = argv[1]):
    return host.lstrip("www.")

def send_receive(client):
    host = get_host_name()
    request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
    client.send(bytes(request, "utf-8"))
    response = client.recv(4096)
    return response

def run():
    sock = connect_socket(create_socket(), argv[1])
    response = send_receive(sock).decode("utf-8")

    print(response)


if __name__ == '__main__':

    validate()
    run()
    


