#!/usr/bin/env python
import time, progressbar

def main():

	bar = progressbar.ProgressBar()

	for i in bar(range(100)):
		time.sleep(0.02)	

if __name__ == '__main__':
	main()
