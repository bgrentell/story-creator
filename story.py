import json

passages = {}

try:
    with open('passages.json') as p: # Loads the passages file into dictonary object.
        passages = json.load(p)
except FileNotFoundError:
    print("Could not find the passages file.  Please make sure it exists!")
    exit(0)
    
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
        
def main():
    # Loops through story until an end result is reached.
    current_passage = "begin" # The tag for the beginning passage
    while current_passage != "end": # The tag for the end of story
        current_passage = do_story(current_passage)
    
def do_story(current_passage):
    # Gets the passage from the global passages list, displays the passage, then returns the next selected passage from the user.
    passage = passages[0][current_passage]
    print_passage(passage["passage"])
    exit(0)

def print_passage(passage):
    # Prints the given passage
    print(passage)
    print()
    
##############
# Test Suite #
##############
# test_path = ["first", "second", "fourth", "end"] # Tests supposed options by the user.

# text = serialize(test_path)
# writeStory(text, "teststory.txt")

if __name__ == '__main__':
    main()
