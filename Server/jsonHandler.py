import json
import os

#E: A users json
#S: None
#D: Writes a json into a file
def writeJSON(jsonObject):
    fileName = jsonObject["user"] + ".json"
    dir = os.path.dirname(__file__)
    completeName = os.path.join(dir, 'Drives', fileName)
    with open(completeName, "w") as outfile:
        json.dump(jsonObject, outfile)
    return

#E: A users username
#S: The users json
#D: Reads a json into a dictionary
def readJSON(user):
    fileName = user + ".json"
    dir = os.path.dirname(__file__)
    completeName = os.path.join(dir, 'Drives', fileName)
    with open(completeName, 'r') as openfile:
        jsonObject = json.load(openfile)
    return jsonObject

#E: A users username and a size in bytes
#S: A new empty json for the user
#D: Returns a new json drive for a user
def newDrive(username, size):
    jsonObject = {
        "user": username,
        "size": size,
        "used": 0,
        "root": {
            "directories": [],
            "files": []
        },
        "shared": {
            "directories": [],
            "files": []
        }
    }
    return jsonObject

def createDrive(username, size):
    #check for unique username
    jsonObject = newDrive(username, size)
    writeJSON(jsonObject)
    return

