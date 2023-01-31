from flask import Blueprint

about_bp = Blueprint('about', __name__)

@about_bp.route('/example/')
def example():
    return "This is the home page"
