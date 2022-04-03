#!/usr/bin/env python
import sys
sys.path.append("/home/wisp/Lab/repos/personal/python_learning/pcap/review/module_5/modules/append_import/modules")
from hello import Hello, say_bye

if __name__ == '__main__':

	new_greeting = Hello()

	new_greeting.say_hi()
	say_bye()
