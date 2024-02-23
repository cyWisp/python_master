import logging

from flask import Flask
from markupsafe import escape


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

# Configuring logging for the flask application
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.INFO)


# show the user profile for that user
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'


# show the post with the given id, the id is an integer
@app.route('/post/<int:post_id>')
def show_post(post_id):
    log.info(f'the post ID: {post_id}')

    return f'Post {post_id}'


# show the subpath after /path/
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    log.info(f'Custom logging message: {subpath}')

    return f'Directory content: {subpath}'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=1234,
        debug=True
    )
