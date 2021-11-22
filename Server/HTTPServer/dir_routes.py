# Imports
from server import app
from flask import request, jsonify, make_response
from flask_expects_json import expects_json
from JSONHandler.fileHandler import getDirContent

# Request schemas
get_dir_req_schema = {
    "type": "object",
    "properties": {
        "dirPath": {"type": "string"},
    },
    "required": ["dirPath"]
}


# Routes
# Route to get a specific dir of an user
@app.route('/dirs', methods=['GET'])
@expects_json(get_dir_req_schema)
def get_dir():
    """
    response:
    {
        "username": String,
        "contents": [
            "directories": [
                {
                    "name": String,
                    "directories": Array,
                    "files": String
                }
            ]
            "files" [
             {
                "name": String,
                "extension": String,
                "creation": String  (YYYY-MM-DD HH:MM:SS),
                "modification": String (YYYY-MM-DD HH:MM:SS),
                "size": Number,
                "content": String
            }
            ]
        ]
    }
    """
    content = request.json
    resp = getDirContent(content["dirPath"])
    return make_response(jsonify(resp), 200)
