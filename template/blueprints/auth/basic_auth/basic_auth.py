# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('basic-auth', __name__, url_prefix='/basic-auth')

@bp.route('/')
def index():
    return '/auth/basic-auth'

from .sqlite_auth import sqlite_auth_bp
bp.register_blueprint(sqlite_auth_bp)