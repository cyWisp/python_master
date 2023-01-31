#!/usr/bin/env python
from flask import Flask
from flask import jsonify

app = Flask(__name__)


# Basic example - Returns string
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return 'Hello, from index...'


# This example will capture an integer from
# the given URL to be used as a variable.
@app.route('/<int:number>')
def incrementer(number):
    return f'Incremented number is {number + 1}'


# This example will capture a string from
# the given URL to be used as a variable.
@app.route('/<string:name>')
def hello_name(name):
    return f"Hello, {name}"


# This example will return a json response.
@app.route('/person')
def hello_person():
    return jsonify({'name': 'Rob', 'age': 37, 'location': 'Miami'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
