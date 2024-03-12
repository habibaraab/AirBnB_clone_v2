#!/usr/bin/python3
""" 0. Script to start a Flask web application """

from flask import Flask, render_templete


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns some text. """
    return render_templete("10-hbnb_filters.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
