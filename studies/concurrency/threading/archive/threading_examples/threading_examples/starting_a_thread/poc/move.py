#!/usr/bin/env python
import os, shutil

if __name__ == '__main__':

	for f in os.listdir("./orig"):
		shutil.move(os.path.join(os.path.abspath("./orig"), f), os.path.join(os.path.abspath("./dest"), f))
