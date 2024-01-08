#!/usr/bin/python3
"""Module for defining the routes related to
the status of the API"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Route handler for the API
    Returns a JSON response with key "status set to OK"
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_ofObjects():
    """Retrieves the number of each object type
    returns key-value pairs where value is the number of objects"""
    return jsonify(amenities=storage.count("Amenity"),
                   cities=storage.count("City"),
                   places=storage.count("Place"),
                   reviews=storage.count("Review"),
                   states=storage.count("State"),
                   users=storage.count("User"))
