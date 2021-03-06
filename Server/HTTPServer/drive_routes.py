# Imports
from HTTPServer import app
from flask import request, jsonify, make_response
from flask_expects_json import expects_json
from JSONHandler.loginHandler import createDrive, login, driveIsUnique, getSpace, getUsers

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
# Route to create a new drive with a new username
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
    if not driveIsUnique(content["username"]):
        error = {"message": "Another drive already exists with given username"}
        return make_response(jsonify(error), 409)
    if not type(content["requestedBytes"]) == int:
        error = {"message": "Please enter an integer amount of bytes to allocate for the drive"}
        return make_response(jsonify(error), 409)
    status = createDrive(content["username"], content["password"], content["requestedBytes"])
    if not status:
        error = {"message": "Invalid username, please try another"}
        return make_response(jsonify(error), 409)
    resp = {"username": content["username"], "allocatedBytes": content["requestedBytes"]}
    return make_response(jsonify(resp), 200)


# Route to login a drive user
@app.route('/drives/login', methods=['POST'])
@expects_json(post_drive_login_req_schema)
def post_drive_login():
    """
    response:
    {
        status: boolean
    }
    """
    content = request.json
    status = login(content["username"], content["password"])
    if not status:
        error = {"status": False, "message": "Invalid username or password, please try another"}
        return make_response(jsonify(error), 409)
    resp = {"status": True}
    return make_response(jsonify(resp), 200)


# Route to get the available space of a Drive
@app.route('/drives/spaces', methods=['GET'])
def get_drive_space():
    """
    Params:
        username
    response:
    {
        username: String,
        usedSpace: Number.
        totalSpace: Number
    }
    """
    drive_username = request.args.get('username')
    if drive_username is None:
        error = {"message": "Given URL has no username drive attribute"}
        return make_response(jsonify(error), 408)
    drive_space = getSpace(drive_username)
    resp = {"username": drive_username, "usedSpace": drive_space[1], "totalSpace": drive_space[0]}
    return make_response(jsonify(resp), 200)


# Route to get all the existing usernames with drives
@app.route('/drives', methods=['GET'])
def get_drive():
    """
    response:
    {
        users: [String],
    }
    """
    return make_response(jsonify(getUsers()), 200)
