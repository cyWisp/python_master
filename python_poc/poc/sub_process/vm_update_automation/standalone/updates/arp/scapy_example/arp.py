#!/usr/bin/env python
from scapy.all import *
from sys import argv, exit

VM_NET = '192.168.251.1/24'
WIFI = '10.0.0.1/24'

def scan(ip):
	arp_req_frame = scapy.ARP(pdst = ip)
	broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

	answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout=1, verbose=False)[0]
	result = []

	for i in range(0, len(answered_list)):
		client_dict = {"ip": answered_list[i][1].psrc, "mac": answered_list[i][1].hwsrc}
		result.append(client_dict)

	return result

if __name__ == '__main__':
	
	scanned_output = scan(VM_NET)

	for i in scanned_output:
		print(i)
	
