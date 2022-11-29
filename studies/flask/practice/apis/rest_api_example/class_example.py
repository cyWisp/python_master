from flask import Flask
from flask_classful import flaskView

app = Flask(__name__)

class TestView(FlaskView):
    def index(self):
        return 'this is just a test'


TestView.register(app, route_base='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)