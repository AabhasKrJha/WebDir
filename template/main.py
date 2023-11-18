# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import os


def create_app(testing = False):

    """app factory"""

    app = Flask(__name__)

    # app context manager
    app_ctx = app.app_context()
    app_ctx.push()

    app.config["SECRET_KEY"] = "this is a secret key"


    CWD = os.getcwd()

    BASIC_AUTH_SQLITE_DATABSE_URI = os.path.join(CWD, 'blueprints/auth/basic_auth/sqlite_db.db')
    app.config['BASIC_AUTH_SQLITE_DATABSE_URI'] = BASIC_AUTH_SQLITE_DATABSE_URI

    # debug mode on while testing the app or when in development mode
    if testing:
        app.debug = True


    # flask app routes
    
    @app.route("/")
    # root route
    def index():
        """Landing page of the app"""
        return render_template("index.html")


    @app.route("/about")
    # about page
    def about():
        """about page of the app"""
        return render_template("about.html")

    
    @app.route('/sitemap')
    # sitemap
    def routes():
        """displays all the routes for the app"""
        routes = {}
        for rule in app.url_map.iter_rules():
            if rule.endpoint != "static":
                routes[rule.rule] = app.view_functions[rule.endpoint].__doc__
        endpoints = list(routes.keys())
        endpoints.sort()
        return render_template('routes.html', routes = routes, endpoints = endpoints)


    # registering blueprints

    #components blueprint
    from blueprints.components import componentsBP
    app.register_blueprint(componentsBP.bp)

    # authentication blueprint
    from blueprints.auth import authBP
    app.register_blueprint(authBP.bp)

    from blueprints.auth.basic_auth import sqlite_db
    sqlite_db.init_app(app)
    sqlite_db.init_db()
    

    return app


if __name__  == "__main__":
    FLASK_APP = create_app(testing = True)
    FLASK_APP.run(port = 5000)