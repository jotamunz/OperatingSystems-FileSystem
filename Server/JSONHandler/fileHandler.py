from JSONHandler.jsonHandler import *

#E: A string path beginning with the username
#S: A json with the paths name, directories and files
#D: Returns the folders and files of a path
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
            found = False
            for directory in jsonObject["directories"]:
                if directory["name"] == folder:
                    jsonObject = directory
                    found = True
            if not found:
                return {}
    return jsonObject