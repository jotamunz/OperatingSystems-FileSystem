# Imports
from HTTPServer import app
from flask import request, jsonify, make_response
from JSONHandler.fileHandler import getDirContent
from flask_expects_json import expects_json

post_dir_req_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "newDirPath": {"type": "number"},
        "dirName": {"type": "string"}
    },
    "required": ["username", "newDirPath", "dirName"]
}


# Routes
# Route to get a specific dir of an user
@app.route('/dirs', methods=['GET'])
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
    contents is empty in case of error
    }
    """
    dir_path = request.args.get('dirPath')
    resp = getDirContent(dir_path)
    if not resp:
        return make_response(jsonify(resp), 409)
    return make_response(jsonify(resp), 200)


# Route to create a file
@app.route('/dirs', methods=['POST'])
@expects_json(post_dir_req_schema)
def post_dir():
    """
    response:
    {
        "username": String
        "dirName": String,
        "path": String,
    }
    """
    content = request.json
    resp = {}
    return make_response(jsonify(resp), 200)
