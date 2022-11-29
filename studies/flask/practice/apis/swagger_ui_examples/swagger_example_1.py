import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/hello/')
class HelloWorld(Resource):
    def get(self):
        return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)