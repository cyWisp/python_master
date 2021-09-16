#!/usr/bin/env python
import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.dest = (self.host, self.port)
        self.client = None
        self.request = None
        self.response = None

    def s_create(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def s_connect(self):
        self.client.connect(self.dest)

    def s_send(self):
        self.format_request()
        self.client.send(self.request)

    def s_receive(self):
        self.response = self.client.recv(4096)

    def format_request(self):
        hostname = self.host.lstrip("www.")
        raw_request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\n\r\n"
        self.request = bytes(raw_request, "utf-8")



