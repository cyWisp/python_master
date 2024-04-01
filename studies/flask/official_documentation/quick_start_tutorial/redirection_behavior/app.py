import logging
from flask import Flask
from markupsafe import escape


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


@app.route('/index')
def index():
    log.info('This is the index page.')
    return '<p>This is the index page.</p>'


@app.route('/other/')
def other():
    log.info('This is the index page.')
    return '<p>This is the index page.</p>'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=1111,
        debug=True
    )