#!/usr/bin/env python
import socket

class Client:
    def __init__(self, host, port, data):
        self.host = host
        self.port = port
        self.data = data
        self.dest = (self.host, self.port)
        self.client = None

    def s_create(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def s_send(self):
        self.client.sendto(bytes(self.data, "utf-8"), self.dest)
    
    def s_receive(self):
        data, addr = self.client.recvfrom(4096)
        print(data)

if __name__ == '__main__':

    new_udp = Client("127.0.0.1", 80, "This is some data")
    new_udp.s_create()
    new_udp.s_send()
    new_udp.s_receive()
