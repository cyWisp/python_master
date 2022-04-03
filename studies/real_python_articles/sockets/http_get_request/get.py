#!/usr/bin/env python
import socket
from sys import argv, exit
from bs4 import BeautifulSoup

PORT = 80
TARGET = dict()

def help():
	print(f"[!] Usage: {argv[0]} <HOST> [<PORT>]")
	exit()

def validate():
	if len(argv) < 2 or len(argv) > 3:
		help()
	
def connect(target):
	request = f"GET / HTTP/1.1\r\nHost: {target['HOST']}\r\n\r\n".encode("utf-8")

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_object:
		s_object.connect((target['HOST'], target['PORT']))
		s_object.sendall(request)
	
		try:
			response = s_object.recv(4096)
		except Exception as e: print("[x] Error: {e}")
	return response

def parse_response(response):
	r_object = BeautifulSoup(response, 'html.parser').prettify()
	print(f"[*] Server Response:\n{r_object}")

if __name__ == '__main__':
	validate()

	TARGET['HOST'] = argv[1]
	if len(argv) == 3: TARGET['PORT'] = argv[2]
	else: TARGET['PORT'] = 80

	response = connect(TARGET)
	parse_response(response)
		
	
		
		


