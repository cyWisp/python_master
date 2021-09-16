from app import blog

@blog.route("/")
@blog.route("/index")
def index():
	user = {'username': 'Rob'}
	html = '''
		<html>
			<head>
				<title>Microblog</title>
			</head>
			<body>
				<h1>Hello, ''' + user['username'] + '''!</h1>
			</body>
		</html>
	'''
	return html
