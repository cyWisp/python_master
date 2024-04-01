from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


# This illustrates a route at its most basic
@app.route('/')
@app.route('/index')
def home():
    greeting = 'This is another intro to Flask.'

    return f'''
    <p>{greeting}</p>
    '''


@app.route('/<name>')
def greet(name):
    from markupsafe import escape

    return f'<p>Hi {escape(name)}, it\'s great to meet you!</p>'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True
    )
