#!/usr/bin/env python
from flask import Flask, render_template
from config import parser
import logging
import json

cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=cfg.log_level
)
log = logging.getLogger()

app = Flask(__name__)

USER = {'username': 'John'}

@app.route('/')
@app.route('/index')
def index():

    posts = [
        {
            'author': 'John',
            'body': 'this is some text'
        },
        {
            'author': 'Dan',
            'body': 'this is some more text'
        }
    ]

    return render_template('index.html', title='Home', user=USER, posts=posts)

@app.route('/about')
def about():
    about_text = '''This is the about page.
    Thank you for visiting our site!
    ~ the dudes
    '''

    return render_template('about.html', user=USER, about_text=about_text)

@app.route('/table')
def table():
    from data.data_gen import generate
    columns, rows = generate(num_cols=5, num_rows=40)

    return render_template('table.html', columns=columns, rows=rows)




if __name__ == '__main__':
    log.debug(json.dumps(vars(cfg), indent=4))



    app.run(host='0.0.0.0', port=8085, debug=True)