# Yaml
# http://zetcode.com/python/yaml/
# https://pyyaml.org/wiki/PyYAMLDocumentation
yamlContent = None


def setValue(yaml):
    global yamlContent
    yamlContent = yaml


def getContent(key):
    return yamlContent[key]


def setContent(key, value):
    yamlContent[key] = value


def removeContent(key):
    del yamlContent[key]
