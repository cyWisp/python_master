import logging
from flask import Flask, url_for

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


if __name__ == '__main__':
    with app.test_request_context():
        log.info(url_for('index'))
        log.info(url_for('login'))
        log.info(url_for('login', next='/'))
        log.info(url_for('profile', username='Rob Daglio'))