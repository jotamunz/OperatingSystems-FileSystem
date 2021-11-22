# Imports
from server import app
from flask import request, jsonify, make_response
from flask_expects_json import expects_json

# Request schemas
post_drive_req_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "requestedBytes": {"type": "number"},
    },
    "required": ["username", "requestedBytes"]
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
    if content["username"] == "Turq":
        error = {"message": "User drive already exists"}
        return make_response(jsonify(error), 409)
    print(f'A new drive of {content["requestedBytes"]} bytes was created for user {content["username"]}')
    return make_response(jsonify(resp), 200)
