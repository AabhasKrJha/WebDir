# -*- coding: utf-8 -*-

from flask import Flask, render_template

def create_app(testing = False):

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Your secret key here"

    if testing:
        app.debug = True

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    from blueprints import componentsBP
    app.register_blueprint(componentsBP.bp)
    
    return app

if __name__  == "__main__":
    FLASK_APP = create_app(testing = True)
    FLASK_APP.run(port = 5000)