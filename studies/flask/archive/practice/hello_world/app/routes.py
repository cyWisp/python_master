from app import app

HTML = '''<html>
	<head>
		<title>Learning flask</title>
	</head>
	<body>
		<h1>this is a test</h1>
		<p>
			hello, world!!
			<a href='http://cybersherpa.net'>cybersherpa</a>
		</p>
	</body>
</html>
'''

@app.route('/')
@app.route('/index')
def index():
	return HTML
