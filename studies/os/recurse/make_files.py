#!/usr/bin/env python
import os, time, argparse, progressbar

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('-n', type=int, default=0, help='Number of files to create...')
	parser.add_argument('-t', type=str, default=0, help='Type of file to create...')
	args = parser.parse_args()

	num_files = args.n
	file_type = args.t
	

	for number in range(0, num_files):
		while True:
			if file_type == 'txt':
				command = 'touch file_' + str(number) + '.txt'
				break
			elif file_type == 'pdf':
				command = 'touch file_' + str(number) + '.pdf'
				break
			elif file_type == 'docx':
				command = 'touch file_' + str(number) + '.docx'
				break
			else:
				print('[x] Not a supported file type...\n[!] Please select from txt, pdf or docx...')	
		os.system(command)
	print('[*] Generating files...')
	bar = progressbar.ProgressBar()
	for i in bar(range(100)):
		time.sleep(0.009)
	print('[*] Done!')
	time.sleep(3)

if __name__ == '__main__':
	main()
