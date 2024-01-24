#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask


"""Create an instance of the Flask application"""
app = Flask(__name__)


# Route from the main page
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# Check if this script is the main program
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
