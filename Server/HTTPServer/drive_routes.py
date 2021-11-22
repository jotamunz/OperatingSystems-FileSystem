# Imports
from server import app
from flask import request, Response, jsonify, make_response


# Post routes
@app.route('/drives', methods=['POST'])
def post_drive():
    """
    I:
    {
        "Username" : String
        "RequestedBytes" : Number

    }
    O:
    {
        "Username": String
        "AllocatedBytes": Number
    }
    """
    content = request.json
    print(f'A new drive of {content["RequestedBytes"]} bytes was created for user {content["Username"]}')
    resp = {"Username": content["Username"], "AllocatedBytes": content["RequestedBytes"]}
    if content["Username"] == "Turq":
        error = {"message": "User drive already exists"}
        return make_response(jsonify(error), 408)
    return make_response(jsonify(resp), 200)
