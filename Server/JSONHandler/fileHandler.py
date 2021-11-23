from JSONHandler.jsonHandler import *
import datetime

def getDirContent(path):
    folders = path.split("/")
    if isHomeDir(folders):
        return homeDirectory(folders[0])
    jsonObject = readJSON(folders[0])
    return getContentFromPath(folders, jsonObject)

def isHomeDir(folders):
    if len(folders) <= 1:
        return True
    return False

def enterMainDir(folders):
    folders.pop(0)
    mainDir = folders[0]
    folders.pop(0)
    return mainDir

def getContentFromPath(folders, jsonObject):
    mainDir = enterMainDir(folders)
    return recurseDirectories(folders, jsonObject[mainDir])

def dirIsUnique(path, name):
    folders = path.split("/")
    if isHomeDir(folders):
        return True
    jsonObject = readJSON(folders[0])
    directory = getContentFromPath(folders, jsonObject)
    for subDir in directory["directories"]:
        if subDir["name"] == name:
            return False
    return True

def fileIsUnique(path, name):
    folders = path.split("/")
    if isHomeDir(folders):
        return True
    jsonObject = readJSON(folders[0])
    directory = getContentFromPath(folders, jsonObject)
    for file in directory["files"]:
        if file["name"] == name:
            return False
    return True

def spaceAvailable(path, content):
    folders = path.split("/")
    jsonObject = readJSON(folders[0])
    return jsonObject["size"] >= jsonObject["used"] + len(content)

def createDir(path, name):
    folders = path.split("/")
    if isHomeDir(folders):
        return False
    if not nameIsValid(name):
        return False
    jsonObject = readJSON(folders[0])
    directory = getContentFromPath(folders, jsonObject)
    doAction(directory, name, 0, jsonObject)
    writeJSON(jsonObject)
    return True

def deleteDir(path, name):
    folders = path.split("/")
    if isHomeDir(folders):
        return False
    jsonObject = readJSON(folders[0])
    directory = getContentFromPath(folders, jsonObject)
    doAction(directory, name, 1, jsonObject)
    writeJSON(jsonObject)
    return True

def createFile(path, name, extension, content):
    folders = path.split("/")
    if isHomeDir(folders):
        return False
    if not nameIsValid(name) or not nameIsValid(extension):
        return False
    jsonObject = readJSON(folders[0])
    directory = getContentFromPath(folders, jsonObject)
    doAction(directory, name, 2, jsonObject, content, extension)
    writeJSON(jsonObject)
    return True

def deleteFile(path, name):
    folders = path.split("/")
    if isHomeDir(folders):
        return False
    jsonObject = readJSON(folders[0])
    directory = getContentFromPath(folders, jsonObject)
    doAction(directory, name, 3, jsonObject)
    writeJSON(jsonObject)
    return True

def recurseDirectories(folders, jsonObject):
    if len(folders) == 0:
        return jsonObject
    else:
        for i, directory in enumerate(jsonObject["directories"]):
            if directory["name"] == folders[0]:
                return recurseDirectories(folders[1:], directory)
        return jsonObject

def doAction(jsonObject, name, status, jsonHome, content=None, extension=None):
    match status:
        # Create a new directory
        case 0:
            deleteDirByName(jsonObject, name)
            createDirByName(jsonObject, name)
        # Delete a directory
        case 1:
            deleteDirByName(jsonObject, name)
        # Create a new file
        case 2:
            size = deleteFileByName(jsonObject, name)
            addSpace(jsonHome, -size)
            size = createFileByName(jsonObject, name, extension, content)
            addSpace(jsonHome, size)
        # Delete a file
        case 3:
            size = deleteFileByName(jsonObject, name)
            addSpace(jsonHome, -size)
    return

def deleteDirByName(jsonObject, name):
    for i, directory in enumerate(jsonObject["directories"]):
        if directory["name"] == name:
            jsonObject["directories"].pop(i)
            break
    return

def createDirByName(jsonObject, name):
    jsonObject["directories"].append({
        "name": name,
        "directories": [],
        "files": []
    })
    return

def deleteFileByName(jsonObject, name):
    for i, file in enumerate(jsonObject["files"]):
        if file["name"] == name:
            jsonObject["files"].pop(i)
            return file["size"]
    return 0

def createFileByName(jsonObject, name, extension, content):
    jsonObject["files"].append({
        "name": name,
        "extension": extension,
        "creation": datetime.datetime.now().isoformat(),
        "modification": datetime.datetime.now().isoformat(),
        "size": len(content),
        "content": content
    })
    return len(content)

def addSpace(jsonHome, space):
    jsonHome["used"] += space
    return




