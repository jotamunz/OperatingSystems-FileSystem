# Imports
from HTTPServer import app
from flask import request, jsonify, make_response
from JSONHandler.fileHandler import getDirContent, createDir, dirIsUnique, deleteDir, moveDir
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

delete_dir_req_schema = {
    "type": "object",
    "properties": {
        "dirPath": {"type": "string"},
        "dirName": {"type": "string"},
    },
    "required": ["dirPath", "dirName"]
}

post_move_dir_req_schema = {
    "type": "object",
    "properties": {
        "dirPath": {"type": "string"},
        "dirName": {"type": "string"},
        "destinyPath": {"type": "string"},
        "forceOverwrite": {"type": "boolean"}
    },
    "required": ["dirPath", "dirName", "destinyPath", "forceOverwrite"]
}

post_share_dir_req_schema = {
    "type": "object",
    "properties": {
        "dirPath": {"type": "string"},
        "dirName": {"type": "string"},
        "destinyUsername": {"type": "string"},
        "forceOverwrite": {"type": "boolean"}
    },
    "required": ["dirPath", "dirName", "destinyUsername", "forceOverwrite"]
}


# Routes
# Route to get a specific dir of an user
@app.route('/dirs', methods=['GET'])
def get_dir():
    """
    Params:
        dirPath
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
    if dir_path is None:
        error = {"message": "Given URL has no directory path attribute"}
        return make_response(jsonify(error), 408)
    resp = getDirContent(dir_path)
    if not resp:
        error = {"message": "The given directory path doesn't exist"}
        return make_response(jsonify(error), 409)
    return make_response(jsonify(resp), 200)


# Route to create a directory in given path
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


# Route to delete an existing directory
@app.route('/dirs', methods=['DELETE'])
@expects_json(delete_dir_req_schema)
def delete_dir():
    """
    response:
    {
        "dirName": String,
        "dirPath": String,
    }
    """
    content = request.json
    status = deleteDir(content["dirPath"], content["dirName"])
    if not status:
        error = {"message": "The directory doesn't exist"}
        return make_response(jsonify(error), 408)
    resp = {"dirName": content["dirName"], "dirPath": content["dirPath"]}
    return make_response(jsonify(resp), 200)


# Route to move a directory
@app.route('/dirs/move', methods=['POST'])
@expects_json(post_move_dir_req_schema)
def move_dir():
    """
    response:
    {
        "dirName": String,
        "dirPath": String,
        "requestOverwrite": String
    }
    """
    content = request.json
    if not dirIsUnique(content["dirPath"], content["dirName"]) and not content["forceOverwrite"]:
        error = {"message": "Another directory already exists at the shared directory of the target user",
                 "requestOverwrite": True}
        return make_response(jsonify(error), 409)
    status = False
    if not status:
        error = {"message": "The directory could not be moved", "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    resp = {"dirName": content["fileName"], "dirPath": content["filePath"], "requestOverwrite": False}
    return make_response(jsonify(resp), 200)


# Route to share a directory with another user
@app.route('/dirs/share', methods=['POST'])
@expects_json(post_share_dir_req_schema)
def share_dir():
    """
    response:
    {
        "sourceUsername": String
        "destinyUsername": String,
        "sharedDirName": String
    }
    """
    content = request.json
    resp = {"sourceUsername": content["sourceUsername"], "destinyUsername": content["destinyUsername"],
            "sharedDirName": content["dirPath"]}
    return make_response(jsonify(resp), 200)
