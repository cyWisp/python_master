#!/usr/bin/env python
from flask import Flask
import logging

from pages.contact import contact_bp
from pages.home import home_bp
from pages.about import about_bp

logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.DEBUG
)

app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(contact_bp, url_prefix='/contact')
app.register_blueprint(about_bp, url_prefix='/about')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)
