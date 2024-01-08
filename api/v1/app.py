#!/usr/bin/python3
"""Flask application"""
from flask import Flask, make_response, jsonify
import os
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(app_views, url_prefix='/api/v1')
cors = CORS(app, resources={r"/api/*": {"origins": "http://0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(error):
    """Close Storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
