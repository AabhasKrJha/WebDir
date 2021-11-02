# -*- coding: utf-8 -*-

from flask import Blueprint

bp  = Blueprint('flask', __name__, url_prefix='/flask')

BASE_URL = '/components/flask'

@bp.route('/')
def index():
    return BASE_URL

@bp.route('/app-factory')
def app_factory():
    return f"{BASE_URL}/app factory/"