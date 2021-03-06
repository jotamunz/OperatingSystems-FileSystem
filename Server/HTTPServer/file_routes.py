# Imports
from HTTPServer import app
from flask import request, jsonify, make_response
from flask_expects_json import expects_json
from JSONHandler.fileHandler import fileIsUnique, spaceAvailableShareFile, createFile, deleteFile, modifyFile, \
    getFileContent, getFileProperties, moveFile, shareFile, spaceAvailableFile

# Request schemas

post_file_req_schema = {
    "type": "object",
    "properties": {
        "filePath": {"type": "string"},
        "newFileName": {"type": "string"},
        "extension": {"type": "string"},
        "content": {"type": "string"},
        "forceOverwrite": {"type": "boolean"}
    },
    "required": ["filePath", "newFileName", "extension", "content", "forceOverwrite"]
}

post_modify_file_req_schema = {
    "type": "object",
    "properties": {
        "filePath": {"type": "string"},
        "fileName": {"type": "string"},
        "content": {"type": "string"}
    },
    "required": ["filePath", "fileName", "content"]
}

post_move_file_req_schema = {
    "type": "object",
    "properties": {
        "filePath": {"type": "string"},
        "fileName": {"type": "string"},
        "destinyPath": {"type": "string"},
        "forceOverwrite": {"type": "boolean"}
    },
    "required": ["filePath", "fileName", "destinyPath", "forceOverwrite"]
}

delete_file_req_schema = {
    "type": "object",
    "properties": {
        "filePath": {"type": "string"},
        "fileName": {"type": "string"}
    },
    "required": ["filePath", "fileName"]
}

post_share_file_req_schema = {
    "type": "object",
    "properties": {
        "filePath": {"type": "string"},
        "fileName": {"type": "string"},
        "destinyUsername": {"type": "string"},
        "forceOverwrite": {"type": "boolean"}
    },
    "required": ["filePath", "fileName", "destinyUsername", "forceOverwrite"]
}

post_vv_copy_file_req_schema = {
    "type": "object",
    "properties": {
        "filePath": {"type": "string"},
        "fileName": {"type": "string"},
        "destinyPath": {"type": "string"},
        "forceOverwrite": {"type": "boolean"}
    },
    "required": ["filePath", "fileName", "destinyPath", "forceOverwrite"]
}


# Routes
# Route to get properties or content of a file
@app.route('/files', methods=['GET'])
def get_file():
    """
    Params:
        filePath, fileName, contentOnly
    response:
    {
        "fileName": String,
        "extension": String,
        "creation": String,
        "modification": String,
        "size": Number,
        "filePath": String,
        "content": String
    }
    if content = true, only the content field will be sent,
    otherwise response will include all fields
    """
    file_path = request.args.get('filePath')
    if file_path is None:
        error = {"message": "Given URL has no directory path parameter"}
        return make_response(jsonify(error), 408)
    file_name = request.args.get('fileName')
    if file_name is None:
        error = {"message": "Given URL has no file name parameter"}
        return make_response(jsonify(error), 408)
    content = request.args.get('contentOnly')
    if content is None:
        error = {"message": "Given URL has no content only parameter"}
        return make_response(jsonify(error), 408)
    if content == "true":
        resp = getFileContent(file_path, file_name)
        resp = None if resp == "" else {"content": resp}
    else:
        resp = getFileProperties(file_path, file_name)
    if resp is None:
        error = {"message": "The given file doesn't exist"}
        return make_response(jsonify(error), 408)
    return make_response(jsonify(resp), 200)


# Route to create a file
@app.route('/files', methods=['POST'])
@expects_json(post_file_req_schema)
def post_file():
    """
    response:
    {
        "fileName": String,
        "filePath": String,
        "requestOverwrite": Boolean
    }
    """
    content = request.json
    if not fileIsUnique(content["filePath"], content["newFileName"]) and not content["forceOverwrite"]:
        error = {"message": "The given file name already exists", "requestOverwrite": True}
        return make_response(jsonify(error), 409)
    if not spaceAvailableFile(content["filePath"], content["content"]):
        error = {"message": "Sufficient space isn't available in Drive", "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    status = createFile(content["filePath"], content["newFileName"], content["extension"], content["content"])
    if not status:
        error = {"message": "The given file name is invalid, please try another", "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    resp = {"fileName": content["newFileName"], "filePath": content["filePath"], "requestOverwrite": False}
    return make_response(jsonify(resp), 200)


# Route to move a file
@app.route('/files/move', methods=['POST'])
@expects_json(post_move_file_req_schema)
def move_file():
    """
    response:
    {
        "fileName": String,
        "filePath": String,
        "requestOverwrite": String
    }
    """
    content = request.json
    if not fileIsUnique(content["filePath"], content["fileName"]) and not content["forceOverwrite"]:
        error = {"message": "Another file already exists at destination with the same name", "requestOverwrite": True}
        return make_response(jsonify(error), 409)
    status = moveFile(content["filePath"], content["fileName"], content["destinyPath"])
    if not status:
        error = {"message": "The file could not be moved", "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    resp = {"fileName": content["fileName"], "filePath": content["filePath"], "requestOverwrite": False}
    return make_response(jsonify(resp), 200)


# Route to modify a file
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
    if not spaceAvailableFile(content["filePath"], content["content"]):
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
@app.route('/files/share', methods=['POST'])
@expects_json(post_share_file_req_schema)
def share_file():
    """
    response:
    {
        "destinyUsername": String,
        "sharedFileName": String

    }
    """
    content = request.json
    if not fileIsUnique(content["destinyUsername"] + "/shared", content["fileName"]) and not content["forceOverwrite"]:
        error = {"message": "Another file already exists at the shared folder of target user",
                 "requestOverwrite": True}
        return make_response(jsonify(error), 409)
    if not spaceAvailableShareFile(content["destinyUsername"], content["filePath"], content["fileName"]):
        error = {"message": "Sufficient space isn't available in target user shared directory",
                 "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    status = shareFile(content["filePath"], content["fileName"], content["destinyUsername"])
    if not status:
        error = {"message": "The file could not be shared", "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    resp = {"destinyUsername": content["destinyUsername"], "sharedFileName": content["fileName"],
            "requestOverwrite": False}
    return make_response(jsonify(resp), 200)


# Route to make a vv copy of a file
@app.route('/files/vvcopy', methods=['POST'])
@expects_json(post_vv_copy_file_req_schema)
def vv_copy_file():
    """
    response:
    {
        "fileName": String,
        "filePath": String,
        "requestOverwrite": Boolean
    }
    """
    content = request.json
    if not fileIsUnique(content["destinyPath"], content["fileName"]) and not content["forceOverwrite"]:
        error = {"message": "The given file name already exists at target location", "requestOverwrite": True}
        return make_response(jsonify(error), 409)
    if not spaceAvailableShareFile(content["destinyPath"].split("/")[0], content["filePath"], content["fileName"]):
        error = {"message": "Sufficient space isn't available in Drive", "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    status = moveFile(content["filePath"], content["fileName"], content["destinyPath"], True)
    if not status:
        error = {"message": "The file could not be copied", "requestOverwrite": False}
        return make_response(jsonify(error), 409)
    resp = {"fileName": content["fileName"], "filePath": content["filePath"], "requestOverwrite": False}
    return make_response(jsonify(resp), 200)


# Route to make a vv copy of a file
@app.route('/files/vrcopy', methods=['POST'])
def vr_copy_file():
    """
    Params:
        filePath, fileName
    response:
    {
        "fileName": String,
        "filePath": String,
    }
    """
    content = request.json
    original_file_name = content["fileName"]
    if not fileIsUnique(content["destinyPath"], content["fileName"]):
        i = 1
        while not fileIsUnique(content["destinyPath"], content["fileName"]):
            content["fileName"] = content["fileName"] + f'({str(i)})'
            i += 1
    if not spaceAvailableShareFile(content["destinyPath"].split("/")[0], content["filePath"], original_file_name):
        error = {"message": "Sufficient space isn't available in the drive"}
        return make_response(jsonify(error), 409)
    status = moveFile(content["filePath"], content["fileName"], content["destinyPath"], True)
    if not status:
        error = {"message": "The file could not be copied"}
        return make_response(jsonify(error), 409)
    resp = {"fileName": content["fileName"], "filePath": content["filePath"]}
    return make_response(jsonify(resp), 200)
