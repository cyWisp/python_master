#!/usr/bin/env python

from scapy.all import (
    ARP,
    Ether,
    srp,
)

if __name__ == '__main__':
    
    # set target ip
    target_ip = '10.0.0.1/24'

    # create an ARP packet
    arp = ARP(pdst=target_ip)

    # create the Ether broadcast packet
    # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting

    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # stack them
    packet = ether/arp

    result = srp(packet, timeout=3)[0]

    clients = list()

    for sent, received in result:
        # for each response, append ip and mac address to 'clients' list
        clients.append(f"ip: {received.psrc} | mac: {received.hwsrc}")

    for c in clients:
        print(c)
