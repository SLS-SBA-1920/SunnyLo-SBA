import os.path
import json
import yaml
import shutil
from data.storage import setValue as storageSetValue
from data.config import setValue as configSetValue

hasAdmin = False


def init():
    global hasAdmin
    startInitGUI = False
    if os.path.exists("data/data.json"):
        print("Opening the JSON file")
        f = open('data/data.json')
        jsonContent = json.load(f)
        f.close()
        storageSetValue(jsonContent)
        hasAdmin = False
        if jsonContent.get("users") == None:
            hasAdmin = False
        else:
            for users in jsonContent.get("users"):
                if users.get("admin"):
                    hasAdmin = True
                    break
    else:
        print("Creating the JSON file")
        storageSetValue(json.loads("{}"))
        with open('data/data.json', 'w') as f:
            json.dump({}, f)
        startInitGUI = True

    if not hasAdmin:
        startInitGUI = True

    if os.path.exists("../config.yml"):
        print("Opening the Yaml file")
        with open('../config.yml') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            configSetValue(data)
    else:
        print("Creating the Yaml file")
        with open('data/configDefault.yml') as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            configSetValue(data)
        startInitGUI = True
        shutil.copyfile("data/configDefault.yml", "../config.yml")

    if startInitGUI:
        # start init gui stuff
        from packages.gui import startGUI
        startGUI(True)
        return False
    else:
        return True
