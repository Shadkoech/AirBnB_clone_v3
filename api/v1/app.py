#!/usr/bin/python3
"""
Python script that starts up a web application
"""

from os import getenv
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """Method ending the current running
    SQLAlchemy Session"""
    return storage.close()


@app.errorhandler(404)
def not_found(error):
    """Response when client tries to access a route/endpoint/resource
    that does not exist """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"
    port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)
