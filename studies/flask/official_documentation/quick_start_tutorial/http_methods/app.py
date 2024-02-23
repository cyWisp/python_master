import logging

from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'the method is POST'
    else:
        return 'the method is GET'


@app.get('/index')
def index_get():
    return 'get index'


@app.post('/index')
def index_post():
    return 'post index'


if __name__ == '__main__':

    # with app.test_request_context():
    #     log.info(f'The url for login is {url_for("login")}')

    app.run(
        host='0.0.0.0',
        port=1234,
        debug=True
    )

