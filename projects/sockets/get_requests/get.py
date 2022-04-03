#!/usr/bin/env python
import socket, argparse
from bs4 import BeautifulSoup as bs

def get_target():

    parser = argparse.ArgumentParser()
    parser.add_argument('target_host', type=str, default='', help='Target host...')
    parser.add_argument('target_port', type=int, default='', help='Target port...')
    args = parser.parse_args()
    
    target = ((args.target_host, args.target_port))

    return target

if __name__ == '__main__':

    target = get_target()
    request = "GET / HTTP/1.1\r\nHost: {0}\r\n\r\n".format(target[0]).encode("utf-8")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target[0], target[1]))
    sock.sendall(request)
    response = sock.recv(4096)

    f_response = bs(response, 'html.parser')

    if response:
        print("[*] Server response: \n{0}".format(f_response.prettify()))
    else:
        print("[!] Unable to connect to server...")

