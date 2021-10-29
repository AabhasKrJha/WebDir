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
    
    return app

if __name__  == "__main__":
    app = create_app(testing = True)
    app.run(port = 5000)