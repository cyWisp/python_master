from flask import Blueprint

home_bp = Blueprint('home', __name__)

@home_bp.route('/example/')
def example():
    return "This is the home page"
