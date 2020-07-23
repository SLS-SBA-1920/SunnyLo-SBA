import os


def deleteFile(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)


deleteFile("../config.yml")
deleteFile("data/data.json")

print("Data reset")
