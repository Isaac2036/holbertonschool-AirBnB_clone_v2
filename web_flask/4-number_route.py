#!/usr/bin/python3
"""Corriendo web service con flask"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Esta ruta muestra un saludo en el home"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Nuestro primer recurso"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Nuestro primera variable"""
    cleaned_text = text.replace('_', ' ')
    return f"C {cleaned_text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_is_cool(text='is cool'):
    """Python si es genial!!!"""
    cleaned_text = text.replace('_', ' ')
    return f"Python {cleaned_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_it_a_number(n):
    """Python si es genial!!!"""
    if isinstance(n, int):
        return f"{n} a is number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
