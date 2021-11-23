from JSONHandler.jsonHandler import *

def homeDirectory(username):
    return {
        "name": username,
        "directories":
        [
            {
                "name": "root",
                "directories": [],
                "files": []
            },
            {
                "name": "shared",
                "directories": [],
                "files": []
            }
        ],
        "files": []
    }

# E: A string path beginning with the username
# S: A json with the paths name, directories and files
# D: Returns the folders and files of a path
def getDirContent(path):
    folders = path.split("/")
    jsonObject = getDriveFromFolders(folders)
    folders.pop(0)
    return getContentFromFolders(folders, jsonObject)

def getDriveFromFolders(folders):
    jsonObject = readJSON(folders[0])
    if len(folders) <= 1:
        jsonObject = homeDirectory(folders[0])
    return jsonObject

def getContentFromFolders(folders, jsonObject):
    if len(folders) > 0:
        jsonObject = jsonObject[folders[0]]
        folders.pop(0)
    for folder in folders:
        found = False
        for directory in jsonObject["directories"]:
            if directory["name"] == folder:
                jsonObject = directory
                found = True
        if not found:
            return {}
    return jsonObject

def dirIsUnique(path, name):
    folders = path.split("/")
    jsonObject = getDriveFromFolders(folders)
    folders.pop(0)
    jsonObject = getContentFromFolders(folders, jsonObject)
    for directory in jsonObject["directories"]:
        if directory["name"] == name:
            return False
    return True

def createDir(path, name):
    if nameIsValid(name):
        folders = path.split("/")
        jsonObject = readJSON(folders[0])
        if len(folders) <= 1:
            return False
        folders.pop(0)
        mainDir = folders[0]
        folders.pop(0)
        jsonObject[mainDir] = createDirRecursive(folders, name, jsonObject[mainDir])
        writeJSON(jsonObject)
        return True
    return False

def createDirRecursive(folders, name, jsonObject):
    if len(folders) == 0:
        for i, directory in enumerate(jsonObject["directories"]):
            if directory["name"] == name:
                jsonObject["directories"].pop(i)
        jsonObject["directories"].append({
            "name": name,
            "directories": [],
            "files": []
            })
        return jsonObject
    else:
        for i, directory in enumerate(jsonObject["directories"]):
            if directory["name"] == folders[0]:
                jsonObject["directories"][i] = createDirRecursive(folders[1:], name, directory)
                return jsonObject
        return jsonObject

def deleteDir(path, name):
    if nameIsValid(name):
        folders = path.split("/")
        jsonObject = readJSON(folders[0])
        if len(folders) <= 1:
            return False
        folders.pop(0)
        mainDir = folders[0]
        folders.pop(0)
        jsonObject[mainDir] = deleteDirRecursive(folders, name, jsonObject[mainDir])
        writeJSON(jsonObject)
        return True
    return False

def deleteDirRecursive(folders, name, jsonObject):
    if len(folders) == 0:
        for i, directory in enumerate(jsonObject["directories"]):
            if directory["name"] == name:
                jsonObject["directories"].pop(i)
        return jsonObject
    else:
        for directory in jsonObject["directories"]:
            if directory["name"] == folders[0]:
                return createDirRecursive(folders[1:], name, directory)
        return jsonObject