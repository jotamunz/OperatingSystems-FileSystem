import json
import os
import string

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

#E: A fisical directory and a file name
#S: A boolean
#D: Determines if a file exists in a fisical directory
def fileExistsFisical(directory, name):
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file):
            base = os.path.basename(file)
            fileName = os.path.splitext(base)[0]
            if fileName == name:
                return True
    return False

#E: A file name
#S: A boolean
#D: Determines if a file name contains special characters
def nameIsValid(name):
    invalidChars = set(string.punctuation.replace(" ", ""))
    return not any(char in invalidChars for char in name)

def getContentNamesFisical(directory):
    names = []
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file):
            base = os.path.basename(file)
            fileName = os.path.splitext(base)[0]
            names.append(fileName)
    return names

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