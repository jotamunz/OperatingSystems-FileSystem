import json
import os

#E: A users json
#S: None
#D: Writes a json into a file
def writeJSON(jsonObject):
    fileName = jsonObject["user"] + ".json"
    directory = os.path.dirname(__file__)
    completeName = os.path.join(directory, '..', 'Drives', fileName)
    with open(completeName, "w") as outfile:
        json.dump(jsonObject, outfile)
    return

#E: A users username
#S: The users json
#D: Reads a json into a dictionary
def readJSON(user):
    fileName = user + ".json"
    directory = os.path.dirname(__file__)
    completeName = os.path.join(directory, '..', 'Drives', fileName)
    with open(completeName, 'r') as openfile:
        jsonObject = json.load(openfile)
    return jsonObject

def fileIsUnique(directory, newFileName):
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file):
            base = os.path.basename(file)
            fileName = os.path.splitext(base)[0]
            if fileName == newFileName:
                return False
    return True

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

#E: A users username and a size in bytes
#S: A boolean indicating success
#D: Creates a new drive for a user if his username is unique
def createDrive(username, size):
    currentDir = os.path.dirname(__file__)
    drivesDir = os.path.join(currentDir, '..', 'Drives')
    #validate username
    if fileIsUnique(drivesDir, username):
        jsonObject = newDrive(username, size)
        writeJSON(jsonObject)
        return True
    return False

