# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('basic auth', __name__, url_prefix='/auth')

BASE_URL = '/basic-auth'

@bp.route('/')
def index():
    return BASE_URL

from .basic_auth import basic_auth
bp.register_blueprint(basic_auth.bp)