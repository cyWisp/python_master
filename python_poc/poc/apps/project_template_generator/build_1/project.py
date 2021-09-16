#!/usr/bin/env python

from os import system
from sys import exit, argv
from time import sleep

def write_file(template, file_name):

	try:
		with open(file_name, 'w+') as new_file:
			new_file.write(template)
	except:
		print("[x] Unable to open file for writing!")
		exit(0)
	finally:
		new_file.close()
		

def python_project(project_name):

	print('[*] Generating new Python project!')
	print(f'[*] Creating {project_name}.py...')
	sleep(1)

	python_file = """#!/usr/bin/env python
import os, sys

if __name__ == '__main__':
	# New Project!
"""
	file_name = f"{project_name}.py"
	write_file(python_file, file_name)
	
	print('[*] Done!')

def javascript_project(project_name):

	print('[*] Generating new Javascript project!')
	print(f'[*] Creating {project_name}.html...')
	print(f'[*] Creating {project_name}.js...')
	sleep(1)
	
	index = f"""<!DOCTYPE html>
<html lang='en'>
<html>
	<head>
		<meta charset='utf-8'>
		<title>New Project</title>
	</head>
	<body>
		<p>New Project!</p>
		<script type="text/javascript" src="./{project_name}.js"></script>
	</body>
</html>
"""
	jscript = """// New Project
"""
	index_fileName = f"{project_name}.html"
	jscript_fileName = f"{project_name}.js"

	write_file(index, index_fileName)
	write_file(jscript, jscript_fileName)

	print("[*] Done!")

if __name__ == '__main__':

	if len(argv) is not 3:
		print(f"[!] Usage: {argv[0]} [-j or -p] <project_name>")
		exit(0)
	else:
		if argv[1] == '-j':
			system('clear')
			sleep(1)
			javascript_project(argv[2])
			exit(0)
		elif argv[1] == '-p':
			system('clear')
			sleep(1)
			python_project(argv[2])
		else:
			print("[!] Please include a project type [-j (javascript) or -p (python)")
			exit(0)
			
			

	

	
	
