# -*- coding: utf-8 -*-

from flask import Blueprint

bp  = Blueprint('components', __name__, url_prefix='/components')

@bp.route('/')
def index():
    return '/components'

from .flaskBP import flask_components
bp.register_blueprint(flask_components.bp)

from .bootstrapBP import bootstrap_components
bp.register_blueprint(bootstrap_components.bp)