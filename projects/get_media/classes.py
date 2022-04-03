#!/usr/bin/env python
from requests import (
    get,
    ConnectionError,
    HTTPError,
)

"""
Insert insightful comments here...
"""

class ScriptArgs:
    def __init__(self, arg_list):
        self.arg_list = arg_list
        self.audio_switch = False
        self.arg_list_len = len(self.arg_list)

    def usage(self):
        print(f"[!] Usage: {self.arg_list[0]} [-a] <URL>")
        print("[?] -a [Extract Audio]: Will download media audio only...")
        quit()

    def validate_url(self):
        print("[+] Validating URL...")
        if self.audio_switch: url = self.arg_list[2]
        else: url = self.arg_list[1]

        try: r = get(url)
        except (ConnectionError, HTTPError) as e: 
            print("[x] Invalid URL!")
            quit()
        else:
            if r.status_code == 200: pass

    def validate(self):
        print("[+] Validating command line arguments...")
        if self.arg_list_len < 2 or self.arg_list_len > 3:
            self.usage()
        else:
            if self.arg_list_len == 2:
                self.audio_switch = False
                self.validate_url()
            elif self.arg_list_len == 3:
                if self.arg_list[1] == "-a":
                    self.audio_switch = True
                    self.validate_url()
                else:
                    print("[x] Invalid switch...")
                    self.usage()



        

