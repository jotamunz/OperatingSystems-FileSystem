from JSONHandler.jsonHandler import *

def DriveIsUnique(username):
    currentDir = os.path.dirname(__file__)
    drivesDir = os.path.join(currentDir, '..', 'Drives')
    return not fileExistsFisical(drivesDir, username)

#E: A users username and a size in bytes
#S: A new empty json for the user
#D: Returns a new json drive for a user
def newDrive(username, password, size):
    jsonObject = {
        "user": username,
        "password": password,
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
#D: Creates a new drive for a user if his username is valid
def createDrive(username, password, size):
    if nameIsValid(username):
        jsonObject = newDrive(username, password, size)
        writeJSON(jsonObject)
        return True
    return False

def login(username, password):
    if nameIsValid(username):
        currentDir = os.path.dirname(__file__)
        drivesDir = os.path.join(currentDir, '..', 'Drives')
        if fileExistsFisical(drivesDir, username):
            jsonObject = readJSON(username)
            if password == jsonObject["password"]:
                return True
    return False
