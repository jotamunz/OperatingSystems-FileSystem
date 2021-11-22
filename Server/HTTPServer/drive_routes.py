# Imports
from server import app
from flask import request, jsonify, make_response
from flask_expects_json import expects_json
from JSONHandler.jsonHandler import *

# Request schemas
post_drive_req_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "requestedBytes": {"type": "number"},
        "password": {"type": "string"}
    },
    "required": ["username", "requestedBytes", "password"]
}

post_drive_login_req_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["username", "password"]
}


# Routes
@app.route('/drives', methods=['POST'])
@expects_json(post_drive_req_schema)
def post_drive():
    """
    response:
    {
        "username": String,
        "allocatedBytes": Number
    }
    """
    content = request.json
    resp = {"username": content["username"], "allocatedBytes": content["requestedBytes"]}
    status = createDrive(content["username"], content["requestedBytes"])
    if not status:
        error = {"message": "Invalid username, please input another one"}
        return make_response(jsonify(error), 409)
    return make_response(jsonify(resp), 200)


@app.route('/drives/login', methods=['POST'])
@expects_json(post_drive_login_req_schema)
def post_drive_login():
    """
    response:
    {
    }
    """
    content = request.json
    resp = {"username": content["username"]}
    return make_response(jsonify(resp), 200)
