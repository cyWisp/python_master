import logging
from flask import (
    Flask,
    render_template,
    request
)


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


@app.route('/index/')
@app.route('/index/<name>')
def index(name=None):
    name = 'Unknown' if not name else name
    return render_template(
        'index.html',
        name=name,
        title='Example Application'
    )


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=1234,
        debug=True
    )