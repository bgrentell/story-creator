import json

passages = {}
readerpath = []

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
    readerpath.append(current_passage)
    print_passage(passage["passage"])
    return get_option(passage["options"])

def print_passage(passage):
    # Prints the given passage
    print(passage)
    print()
    
def get_option(options):
    # Iterate through list of options, enumerate them, 
    # then ask for the selection from the user.  
    # Each option is the next passage to go to.
    i = 0
    optionsavail = []
    for option in options: # Enumerate and print each option
        i = i + 1
        print(f"{i}: {options[option]}")
        optionsavail.append(option)
    
    optionnumber = get_option_number(len(optionsavail))
    
    return optionsavail[optionnumber - 1] # Return the option name

def get_option_number(max_option):
    # Gets the option number from the user bounded by max_option and 0
    optionnumber = 0
    while optionnumber < 1 or optionnumber > max_option:
        optionnumber = int(input("Please select a path: "))
        if optionnumber < 1 or optionnumber > max_option: # If the option selected is outside of bounds, loop again and display error
            print("Invalid Option!")
        
    return optionnumber

    
##############
# Test Suite #
##############
# test_path = ["first", "second", "fourth", "end"] # Tests supposed options by the user.

# text = serialize(test_path)
# writeStory(text, "teststory.txt")

if __name__ == '__main__':
    main()
