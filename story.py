import json

passages = {}

with open('passages.json') as p: # Loads the passages file into dictonary object.
    passages = json.load(p)
    print(passages)
    
test_path = ["first", "second", "fourth", "end"] # Tests supposed options by the user.

def serialize(path):
    fileText = ""
    for option in path:
        if(option == "end"):
            break
        
        fileText += "\n\n" + passages[0][option]["passage"]
    
    print(fileText)

serialize(test_path)
