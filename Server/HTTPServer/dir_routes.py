# Imports
from HTTPServer import app
from flask import request, jsonify, make_response
from JSONHandler.fileHandler import getDirContent, createDir, dirIsUnique
from flask_expects_json import expects_json

post_dir_req_schema = {
    "type": "object",
    "properties": {
        "newDirPath": {"type": "string"},
        "dirName": {"type": "string"},
        "forceOverwrite": {"type": "boolean"}
    },
    "required": ["newDirPath", "dirName", "forceOverwrite"]
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
        "dirName": String,
        "path": String,
        "requestOverwrite": Boolean
    }
    """
    content = request.json
    if not dirIsUnique(content["newDirPath"], content["dirName"]) and not content["forceOverwrite"]:
        error = {"message": "The given directory name already exists", "requestOverwrite": True}
        return make_response(jsonify(error), 409)
    status = createDir(content["newDirPath"], content["dirName"])
    if not status:
        error = {"message": "The given directory name is invalid, please try another", "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    resp = {"dirName": content["dirName"], "path": content["newDirPath"], "requestOverwrite": False}
    return make_response(jsonify(resp), 200)