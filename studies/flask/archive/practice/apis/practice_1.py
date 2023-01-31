#!/usr/bin/env python
from flask import Flask, jsonify
import logging


logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.DEBUG
)

log = logging.getLogger()
app = Flask(__name__)


def hellos():
    return ['Hi there' for x in range(10)]

# Variable rules
@app.route('/<int:num>/')
def mult_by_two(num):
    return f'{num} x 2 = {num * 2}', 405


@app.route('/<string:word>/')
def whats_the_word(word):
    return f'{word} is the word.', 406


# return json objects
@app.route('/person/')
def return_person():
    p = {
        'name': 'Rob',
        'age': '37',
        'location': 'Miami'
    }

    return jsonify(p), 405


@app.route('/getList/')
def get_list():
    new_list = [str(x) for x in range(10)]
    return jsonify(new_list), 501



@app.before_request
def before():
    log.debug('This is executed before the request is processed.')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/')
def index():
    many_hellow = hellos()
    return many_hellow


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)
