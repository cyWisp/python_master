#!/usr/bin/env python
from flask import Flask, jsonify

app = Flask(__name__)


# As a best practice, wrap routes with two forward slashes
# This will ensure a 404 Not Found response is avoided,
# Should the second forward slash not be included in the
# target URL when navigating.
@app.route('/', methods=['GET', 'POST'])
@app.route('/index/') # will redirect from /index
def index():
    return 'Hello from index...'


@app.route('/contact') # will return 404 if typed /contact/
def contact():
    return 'this is the contact page.'


@app.route('/example/', methods=['GET', 'POST'])
def example():
    return 'this is a different return code', 300


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1050)
