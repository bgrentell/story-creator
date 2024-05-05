import json

passages = {}

with open('passages.json') as p:
    passages = json.load(p)
    print(passages)
    
