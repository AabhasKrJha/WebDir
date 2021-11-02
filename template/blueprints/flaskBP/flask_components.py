from flask import Blueprint

bp  = Blueprint('flask', __name__, url_prefix='/flask')

@bp.route('/')
def index():
    return 'localhost:5000/components/flask'

@bp.route('/app-factory')
def app_factory():
    return "app factory"