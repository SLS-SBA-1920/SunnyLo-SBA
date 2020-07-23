# Json
# https://opensource.com/article/19/7/save-and-load-data-python-json
import json

jsonContent = {}


def setValue(jsonA):
    global jsonContent
    jsonContent = jsonA


def getContent(key):
    return jsonContent.get(key)


def setContent(key, value):
    jsonContent[key] = value
    save()


def removeContent(key):
    del jsonContent[key]


def addContent(key, value):
    if jsonContent.get(key) == None:
        jsonContent[key] = []
    jsonContent[key].append(value)
    save()


def save():
    with open('data/data.json', 'w') as f:
        json.dump(jsonContent, f)
