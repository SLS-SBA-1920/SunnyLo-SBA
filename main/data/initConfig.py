import os.path
import json
import yaml
import shutil
from data.storage import setValue as storageSetValue
from data.config import setValue as configSetValue


def init():
    startInitGUI = False
    if os.path.exists("data/data.json"):
        print("Opening the JSON file")
        f = open('data/data.json')
        jsonContent = json.load(f)
        f.close()
        storageSetValue(jsonContent)
    else:
        print("Creating the JSON file")
        storageSetValue(json.loads("{}"))
        with open('data/data.json', 'w') as f:
            json.dump({}, f)
        startInitGUI = True

    if os.path.exists("../config.yml"):
        print("Opening the Yaml file")
        with open('../config.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            configSetValue(data)
    else:
        print("Creating the Yaml file")
        with open('data/configDefault.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
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
