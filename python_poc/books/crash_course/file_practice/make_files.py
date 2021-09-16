#!/usr/bin/env python
import os, argparse, time, sys

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('num_files', type=int, default=0, help='Number of files to create...')
	parser.add_argument('file_type', type=str, default='', help='Type of files to create...')
	parser.add_argument('text', type=str, default='', help='Text to write in each file')
	args = parser.parse_args()

	if args.file_type == 'txt':
		for num in range(0, args.num_files + 1):
			command = 'touch file_{}.{}'.format(str(num), args.file_type)
			os.system(command)
			with open('file_{}.{}', 'w') as make_file:
				make_file.write(args.text)
			make_file.close()
		print('[*] Creating files...')
		time.sleep(1)
		print('[*] Done!')
		time.sleep(1)
	elif args.file_type == 'pdf':
		for num in range(0, args.num_files + 1):
			command = 'touch file_{}.{}'.format(str(num), args.file_type)
			os.system(command)
		print('[*] Creating files...')
		time.sleep(1)
		print('[*] Done!')
		time.sleep(1)

	elif args.file_type == 'html':
		for num in range(0, args.num_files + 1):
			command = 'touch file_{}.{}'.format(str(num), args.file_type)
			os.system(command)
		print('[*] Creating files...')
		time.sleep(1)
		print('[*] Done!')
		time.sleep(1)
	else:
		print('[x] File type not supported...')
		time.sleep(1)
		print('[*] Exiting...')
		time.sleep(1)
		sys.exit(0)

	
if __name__ == '__main__':
	main()
