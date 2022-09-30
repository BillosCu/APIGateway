import json

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

headers = {"Content-Type": "application/json; charset=utf-8"}