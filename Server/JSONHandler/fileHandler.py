from JSONHandler.jsonHandler import *

def getDirContent(path):
    folders = path.split("/")
    jsonObject = readJSON(folders[0])
    if len(folders) == 1:
        jsonObject.pop("password")
        jsonObject.pop("size")
        jsonObject.pop("used")
    else:
        folders.pop(0)
        jsonObject = jsonObject[folders[0]]
        folders.pop(0)
        for folder in folders:
            for directory in jsonObject["directories"]:
                if directory["name"] == folder:
                    jsonObject = directory
    return jsonObject