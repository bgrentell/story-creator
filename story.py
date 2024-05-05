import json

passages = {}

try:
    with open('passages.json') as p: # Loads the passages file into dictonary object.
        passages = json.load(p)
except FileNotFoundError:
    print("Could not find the passages file.  Please make sure it exists!")
    exit(0)
    
test_path = ["first", "second", "fourth", "end"] # Tests supposed options by the user.

def serialize(path):
    fileText = ""
    for option in path:
        if(option == "end"):
            break
        
        fileText += "\n\n" + passages[0][option]["passage"]
    
    return fileText

def writeStory(fileText, filePath):
    try:
        with open(filePath, 'w') as p:
            p.write(fileText)
    except IOError:
        print("There was a problem writing the file.")        
        


text = serialize(test_path)
writeStory(text, "teststory.txt")
