# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('bootstrap', __name__, url_prefix="/bootstrap")
BASE_URL = '/components/bootstrap'


@bp.route('/')
def index():
    return BASE_URL