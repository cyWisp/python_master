#!/usr/bin/env python
#import os
from os import system, mkdir
from time import sleep
from sys import argv, exit

def pause():
	system('clear')
	sleep(1)

def create_file_content(project_name):

	index_html = f"""<!DOCTYPE html>
<html lang="en">
<html>
	<head>
		<meta charset="utf-8">
		<title>{project_name}</title>
		<link rel="stylesheet" type="text/css" href="./assets/css/style.css">
	</head>
	<body>
		<p id="test"></p>
		<!-- Your code here! -->

		<script type="text/javascript" src="./assets/js/script.js"></script>
	</body>
</html>
"""

	style_css = """/* Your code here! */
#test{
	color: red;
}
"""

	script_js = """/* You code here! */
function test(){
	test_tag = document.getElementById('test');
	test_tag.innerHTML = "This is just a test...";
}

test();
"""

	templates = {"index": index_html, "style": style_css, "script": script_js}

	return templates		

def create_file_structure(project_name):

	try:
		mkdir(project_name)
		mkdir(f"{project_name}/assets")
		mkdir(f"{project_name}/assets/css")
		mkdir(f"{project_name}/assets/js")
		mkdir(f"{project_name}/assets/images")
	except FileExistsError as file_error:
		print(f"[x] Something went wrong! | {file_error}")
	finally:
		pass

def file_error():
	print("[x] Unable to write file!")

def create_files(project_name, templates):

	for title, content in templates.items():
		if title == 'index':
			try:
				with open(f'{project_name}/index.html', 'w+') as new_file:
					new_file.write(content)
			except:
				file_error()
			finally:
				new_file.close()
		elif title == 'style':
			try:
				with open(f'{project_name}/assets/css/style.css', 'w+') as new_file:
					new_file.write(content)
			except:
				file_error()
			finally:
				new_file.close()
		elif title == 'script':
			try:
				with open(f'{project_name}/assets/js/script.js', 'w+') as new_file:
					new_file.write(content)
			except:
				file_error()
			finally:
				new_file.close()
		else:
			pass

def run(project_name):

	pause()
	create_file_structure(project_name)
	create_files(project_name, create_file_content(project_name))

if __name__ == '__main__':

	if len(argv) is not 2:
		print(f"[!] Usage: argv[0] <project name>")
		exit(0)
	else:
		run(argv[1])

