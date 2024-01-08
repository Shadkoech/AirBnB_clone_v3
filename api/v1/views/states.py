#!/usr/bin/python3
"""
Script of State objects handling all the default
RESTFul API actions """


from models.state import State
from models import storage
from api.v1.views import app_views
from flask import make_response, jsonify, abort, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def retrieve_states():
    """Obtains a list of all state objects
    """
    all_states = storage.all(State).values()
    states_list = []
    for state in all_states:
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def retrieve_state(state_id):
    """ Obtains a given state by their id
    """
    state = storage.get("State", state_id)
    if not state:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """ Method deleting a specified state by id
    """
    state = storage.get("State", state_id)
    if not state:
        abort(404)

    state.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ Create states using HTTP method 'POST'
    """
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")

    state = state(**data)
    storage.new(state)
    storage.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state():
    """ Updates an existing state using HTTP method 'PUT'
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
