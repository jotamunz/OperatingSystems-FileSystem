# Imports
from HTTPServer import app
from flask import request, jsonify, make_response
from flask_expects_json import expects_json
from JSONHandler.fileHandler import fileIsUnique, spaceAvailable, createFile, deleteFile, modifyFile

# Request schemas

post_file_req_schema = {
    "type": "object",
    "properties": {
        "filepath": {"type": "string"},
        "newFileName": {"type": "string"},
        "extension": {"type": "string"},
        "content": {"type": "string"},
        "forceOverwrite": {"type": "boolean"}
    },
    "required": ["filepath", "newFileName", "extension", "content", "forceOverwrite"]
}

post_modify_file_req_schema = {
    "type": "object",
    "properties": {
        "filePath": {"type": "string"},
        "fileName": {"type": "string"},
        "content": {"type": "string"},
    },
    "required": ["filePath", "fileName", "content"]
}

delete_file_req_schema = {
    "type": "object",
    "properties": {
        "filePath": {"type": "string"},
        "fileName": {"type": "string"},
    },
    "required": ["filePath", "fileName"]
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
    file_path = request.args.get('filePath')
    if file_path is None:
        error = {"message": "Given URL has no directory path parameter"}
        return make_response(jsonify(error), 408)
    file_name = request.args.get('fileName')
    if file_name is None:
        error = {"message": "Given URL has no file name parameter"}
        return make_response(jsonify(error), 408)
    resp = {"Username": ""}
    return make_response(jsonify(resp), 200)


# Route to create a file
@app.route('/files', methods=['POST'])
@expects_json(post_file_req_schema)
def post_file():
    """
    response:
    {
        "fileName": String,
        "path": String,
        "requestOverwrite": Boolean
    }
    """
    content = request.json
    if not fileIsUnique(content["filepath"], content["newFileName"]) and not content["forceOverwrite"]:
        error = {"message": "The given directory name already exists", "requestOverwrite": True}
        return make_response(jsonify(error), 409)
    if not spaceAvailable(content["filepath"], content["newFileName"]):
        error = {"message": "Sufficient space isn't available in Drive", "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    status = createFile(content["filepath"], content["newFileName"], content["extension"], content["content"])
    if not status:
        error = {"message": "The given file name is invalid, please try another", "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    resp = {"fileName": content["newFileName"], "path": content["filepath"], "requestOverwrite": False}
    return make_response(jsonify(resp), 200)


@app.route('/files/modify', methods=['POST'])
@expects_json(post_modify_file_req_schema)
def modify_file():
    """
    response:
    {
        "fileName": String,
        "path": String
    }
    """
    content = request.json
    if not spaceAvailable(content["filePath"], content["fileName"]):
        error = {"message": "Sufficient space isn't available in Drive", "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    status = modifyFile(content["filePath"], content["fileName"], content["content"])
    if not status:
        error = {"message": "The given file could not be modified"}
        return make_response(jsonify(error), 409)
    resp = {"fileName": content["fileName"], "path": content["filePath"]}
    return make_response(jsonify(resp), 200)


# Route to delete an existing file
@app.route('/files', methods=['DELETE'])
@expects_json(delete_file_req_schema)
def delete_file():
    """
    response:
    {
        "fileName": String,
        "path": String,
    }
    """
    content = request.json
    status = deleteFile(content["filePath"], content["fileName"])
    if not status:
        error = {"message": "The file doesn't exist"}
        return make_response(jsonify(error), 408)
    resp = {"fileName": content["fileName"], "path": content["filePath"]}
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
