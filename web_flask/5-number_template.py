#!/usr/bin/python3
"""
Script that starts a Flask web application:
listening on 0.0.0.0, port 5000
with Fifth routes
"""
from flask import Flask, escape, request
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ First Route that display Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Second Route that display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
    """ Third Route that display C and text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text):
    """ Fourth Route that display Python and text """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """ Fifth Route that display Number """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_html(n):
    """ Route that display HTML """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
