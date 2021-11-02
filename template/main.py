# -*- coding: utf-8 -*-

from flask import Flask, render_template
import os

def create_app(testing = False):

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "Your-secret-key-here"

    CWD = os.getcwd()

    BASIC_AUTH_SQLITE_DATABSE_URI = os.path.join(CWD, 'blueprints/auth/basic_auth/sqlite_db.db')
    app.config['BASIC_AUTH_SQLITE_DATABSE_URI'] = BASIC_AUTH_SQLITE_DATABSE_URI

    if testing:
        app.debug = True

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    # registering blueprints

    #components blueprint
    from blueprints.components import componentsBP
    app.register_blueprint(componentsBP.bp)

    # authentication blueprint
    from blueprints.auth import authBP
    app.register_blueprint(authBP.bp)

    from blueprints.auth.basic_auth import sqlite_db
    sqlite_db.init_app(app)
    sqlite_db.init_db(app)
    
    return app

if __name__  == "__main__":
    FLASK_APP = create_app(testing = True)
    FLASK_APP.run(port = 5000)