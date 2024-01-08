#!/usr/bin/python3
"""Module for defining the routes related to
the status of the API"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


app_views.route('/status', methods=['GET'])
def status():
    """Route handler for the API
    Returns a JSON response with key "status set to OK"
    """
    return jsonify({"status": "OK"})
