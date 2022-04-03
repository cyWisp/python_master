####################################################################################
# Title: pingMonster.py
# Purpose: pinMonster will check to see if remote hosts are up with a single ICMP ping request
# Usage: python[3] pingMonster.py [list_of_ips.txt]
# Author: Robert Daglio
# Date: 5/20/2018
####################################################################################

#!/usr/bin/env python
import time, os, argparse

def get_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('ip_list', type=str, default='', help="List of IPs to ping...")
    args = parser.parse_args()

    return args.ip_list

def title():
    
    banner = """
\t\t__________.__                    _____                          __                
\t\t\______   \__| ____    ____     /     \   ____   ____   _______/  |_  ___________ 
\t\t |     ___/  |/    \  / ___\   /  \ /  \ /  _ \ /    \ /  ___/\   __\/ __ \_  __ \\
\t\t |    |   |  |   |  \/ /_/  > /    Y    (  <_> )   |  \\___ \  |  | \  ___/|  | \/
\t\t |____|   |__|___|  /\___  /  \____|__  /\____/|___|  /____ > |__|  \___  >__|   
\t\t                  \//_____/           \/            \/     \/            \/       
    """
    print("{}\n".format(banner))
    print("\t\tAuthor: Rob Daglio\t\t\tVer: 1.1.0\n\n")


def run():

    os.system('clear')
    time.sleep(1)

    title()
    
    ip_file = './' + get_args()
    hosts, results = [], []

    try:
        with open(ip_file, 'r') as ips:
            for ip in ips:
                hosts.append(ip.strip())
    except:
        print("[x] Could not read text file...")
    finally:
        ips.close()

    for host in hosts:
        command = "ping -n 1 {} > ./temp.txt".format(host)
        os.system(command)
    
        with open('./temp.txt', 'r') as temp_file:
            for line in temp_file:
                if line == '\n':
                    pass
                else:
                    results.append(line.strip('\n'))

        temp_file.close()
        os.remove('./temp.txt')

    output = []

    for r in results:
        if not "Received" in r:
            pass
        else:
            r = r.split()
            r[6] = str(r[6].strip(','))
            r[9] = str(r[9])
            if r[6] == "1" and r[9] == "0": 
                output.append("UP")
            else:
                output.append("DOWN")
    
    for index, h in enumerate(hosts):
        print("Host: {} | Status: {} ".format(h, output[index]))
        time.sleep(1)

    print('\n')

if __name__ == '__main__':
    run()
    