import json

fileObject = open("data.json", "r")
jsonContent = fileObject.read()
aList = json.loads(jsonContent)
