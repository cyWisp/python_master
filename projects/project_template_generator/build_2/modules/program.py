from os import system
from time import sleep
from files import create_files, create_file_content, create_file_structure

def pause():
	system('clear')
	sleep(1)

def run(project_name):

	pause()
	create_file_structure(project_name)
	create_files(project_name, create_file_content(project_name))
	sleep(1)
	print("[*] Done!")
