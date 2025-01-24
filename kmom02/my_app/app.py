#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
import traceback
from flask import Flask, render_template
from src.car import Car

app = Flask(__name__)

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@app.route("/about")
def about():
    """ About route """
    my_car = Car("BMW", 90000)
    my_name = "Marie Grahn"
    my_course = "OOPython"

    return render_template("about.html", name=my_name, course=my_course,
        car=my_car)

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run(debug=True)
