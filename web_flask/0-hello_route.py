#!/usr/bin/python3
"""script that starts a Flask web application:

listening on 0.0.0.0, port 5000
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

if __name__ == "__main__":
    # Start the development server and bind to all available interfaces
    app.run(host="0.0.0.0", port=5000)
