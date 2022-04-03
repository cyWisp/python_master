#!/usr/bin/env python
import socket, re
from sys import argv, exit

class Validate():
    def __init__(self, argument_list):
        self.argument_list = argument_list
        if len(self.argument_list) != 3:
            print("[x] Insufficient arguments")
            self.usage()
        else:
            self.host = self.argument_list[1]
            self.port = self.argument_list[2]

    def validate_all(self):
        self.validate_host()
        self.validate_port()

    def usage(self):
        print(f"[!] Usage: {argv[0]} <node> <port>")
        exit()

    def validate_host(self):
        ip_reg = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        site_reg = re.compile(r'\w{1,40}\.\w{1,40}\.\w{1,40}')
        
        ip_match = ip_reg.search(self.host)
        site_match = site_reg.search(self.host)
        
        if ip_match: pass
        elif site_match:
            self.host = self.host.lstrip('www.')
        else:
            print("[x] Please provide a valid host.")
            exit()

    def validate_port(self):        
        if int(self.port) < 0 or int(self.port) > 65535:
            print("[x] Please provide a valid port.")
            exit()
        else: pass

class Client():
    def __init__(self, host, port):
        self.host = host
        self.port = int(port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_socket(self):
        self.client.connect((self.host, self.port))
    
    def send_receive(self):
        request = f"GET / HTTP/1.1\r\nHost: {self.host}\r\n\r\n".encode("utf-8")
        self.client.send(request)
        response = [x for x in str(self.client.recv(4096).decode("utf-8")).split("\n") if x != ""]
        return response

if __name__ == '__main__':
    target = Validate(argv)
    target.validate_all()

    client = Client(target.host, target.port)
    client.connect_socket()
    response = client.send_receive()
    
    for line in response: print(line)
