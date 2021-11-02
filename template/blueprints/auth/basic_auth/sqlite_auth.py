# -*- coding: utf-8 -*-

from flask import Blueprint

sqlite_auth_bp = Blueprint('sqlite-auth', __name__, url_prefix='/sqlite')

@sqlite_auth_bp.route('/')
def index():
    return 'auth/basic-auth/sqlite'