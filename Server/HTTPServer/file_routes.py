# Imports
from HTTPServer import app
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
        "extension": {"type": "string"},
        "content": {"type": "string"}
    },
    "required": ["username", "filepath", "filename", "content", "extension"]
}

put_file_req_schema = {
    "type": "object",
    "properties": {
        "sourceUsername": {"type": "string"},
        "filepath": {"type": "string"},
        "filename": {"type": "string"},
        "destinyUsername": {"type": "string"}
    },
    "required": ["sourceUsername", "filepath", "filename", "destinyUsername"]
}


# Routes
# Route to get properties and content of a file
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
    resp = {"Username": content["Username"], "AllocatedBytes": content["RequestedBytes"]}
    return make_response(jsonify(resp), 200)


# Route to create a file
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
    resp = {"Username": content["Username"], "AllocatedBytes": content["RequestedBytes"]}
    return make_response(jsonify(resp), 200)


# Route to share a file with another user
@app.route('/files', methods=['PUT'])
@expects_json(put_file_req_schema)
def share_file():
    """
    response:
    {
        "sourceUsername": String
        "destinyUsername": String,
        "sharedFilename": String

    }
    """
    content = request.json
    resp = {"sourceUsername": content["Username"], "destinyUsername": content["destinyUsername"],
            "sharedFilename": content["filename"]}
    return make_response(jsonify(resp), 200)
