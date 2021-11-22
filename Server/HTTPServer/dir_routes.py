# Imports
from server import app
from flask import request, jsonify, make_response
from JSONHandler.fileHandler import getDirContent


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
