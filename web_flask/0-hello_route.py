#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return ("Hello HBNB!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

