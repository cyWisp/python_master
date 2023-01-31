from flask import Blueprint

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/example/')
def example():
    return 'this is the contact page'