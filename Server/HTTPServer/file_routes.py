# Imports
from server import app
from flask import request, jsonify, make_response
from flask_expects_json import expects_json

# Request schemas
get_file_req_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "filepath": {"type": "string"},
        "filename": {"type": "string"}
    },
    "required": ["username", "filepath", "filename"]
}

post_file_req_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "filepath": {"type": "string"},
        "filename": {"type": "string"},
        "content": {"type": "string"}
    },
    "required": ["username", "filepath", "filename", "content"]
}


# Routes
@app.route('/files', methods=['GET'])
@expects_json(get_file_req_schema)
def get_file():
    """
    response:
    {
        "name": String,
        "extension": String,
        "creation": String (YYYY-MM-DD HH:MM:SS),
        "modification": String (YYYY-MM-DD HH:MM:SS),
        "size": Number,
        "path": String,
        "content": String
    }
    """
    content = request.json
    print(f'A new drive of {content["RequestedBytes"]} bytes was created for user {content["Username"]}')
    resp = {"Username": content["Username"], "AllocatedBytes": content["RequestedBytes"]}
    if content["Username"] == "Turq":
        error = {"message": "User drive already exists"}
        return make_response(jsonify(error), 409)
    return make_response(jsonify(resp), 200)


@app.route('/files', methods=['POST'])
@expects_json(post_file_req_schema)
def post_file():
    """
    response:
    {
        "username": String
        "filename": String,
        "extension": String,
        "size": Number,
        "path": String,
    }
    """
    content = request.json
    print(f'A new drive of {content["RequestedBytes"]} bytes was created for user {content["Username"]}')
    resp = {"Username": content["Username"], "AllocatedBytes": content["RequestedBytes"]}
    if content["Username"] == "Turq":
        error = {"message": "User drive already exists"}
        return make_response(jsonify(error), 409)
    return make_response(jsonify(resp), 200)
