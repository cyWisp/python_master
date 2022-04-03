#!/usr/bin/env python
import os, argparse, time
from dirsync import sync

def main():

	parseArgs = argparse.ArgumentParser()
	parseArgs.add_argument("dir1", type=str, default="", help="the first string")
	parseArgs.add_argument("dir2", type=str, default="", help="the second string")

	args = parseArgs.parse_args()

	sourceDir = args.dir1
	destDir = args.dir2
	
	print('[*] Gathering data...')
	time.sleep(1)
	print('[*] Now syncing {} and {}...'.format(sourceDir, destDir))
	time.sleep(2)

	sync(sourceDir, destDir, 'sync')

	print('[*] Done!')
	time.sleep(1)

	

if __name__ == '__main__':
	main()
