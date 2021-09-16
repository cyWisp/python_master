from os import mkdir
from time import sleep

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
		print(f"[*] Creating new project: {project_name}...")
		sleep(1)
		mkdir(project_name)
		print(f"[*] Creating {project_name}/assets...")
		sleep(.5)
		mkdir(f"{project_name}/assets")
		print(f"[*] Creating {project_name}/assets/css...")
		sleep(.25)
		mkdir(f"{project_name}/assets/css")
		print(f"[*] Creating {project_name}/assets/js...")
		sleep(.25)
		mkdir(f"{project_name}/assets/js")
		print(f"[*] Creating {project_name}/assets/images...")
		sleep(.25)
		mkdir(f"{project_name}/assets/images")
	except FileExistsError as file_error:
		print(f"[x] Something went wrong! | {file_error}")
	finally:
		pass

def create_files(project_name, templates):

	for title, content in templates.items():
		if title == 'index':
			try:
				print(f"[*] Creating {project_name}/index.html")
				sleep(.5)
				with open(f'{project_name}/index.html', 'w+') as new_file:
					new_file.write(content)
			except:
				print("[x] Unable to write file!")
			finally:
				new_file.close()
		elif title == 'style':
			try:
				print(f"[*] Creating {project_name}/assets/css/style.css...")
				sleep(.25)
				with open(f'{project_name}/assets/css/style.css', 'w+') as new_file:
					new_file.write(content)
			except:
				print("[x] Unable to write file!")
			finally:
				new_file.close()
		elif title == 'script':
			try:
				print(f"[*] Creating {project_name}/assets/js/script.js...")
				sleep(.25)
				with open(f'{project_name}/assets/js/script.js', 'w+') as new_file:
					new_file.write(content)
			except:
				print("[x] Unable to write file!")
			finally:
				new_file.close()
		else:
			pass
