'''
Edit NoMorph.json to make its values
easier to access
'''

import json
from os import path

def edit():
    buildings = {}
    with open('../bldgenergyuse/4 - Simulate buildings for urban morphologies/morphology_data/NoMorph.json', 'r') as jsonFile:
        buildings = json.load(jsonFile)
    
    for id in buildings:
        outputs = buildings[id]["outputs"]
        for key in outputs:
            output = map(lambda x: {x[""]: {key:val for key, val in x.items() if key != "" }}, outputs[key])
            buildings[id]["outputs"][key] = list(output)

    with open('../processed_data/NoMorphEdited.json', 'w') as jsonFile:
        json.dump(buildings, jsonFile)

def iterdict(curr, parent, id, new):
    for k, v in curr.items():
        if isinstance(v, list):
            for item in v:
                iterdict(item, k, id, new)
        elif isinstance(v, dict):
            iterdict(v, k, id, new)
        else:
            if parent == id:
                new[k] = v
            elif len(parent) > 1:
                new[f'{parent} {k}'] = v

def flatten():
    buildings = {}

    if not path.exists('../processed_data/NoMorphEdited.json'):
        edit()
    with open('../processed_data/NoMorphEdited.json', 'r') as jsonFile:
        buildings = json.load(jsonFile)    

    newBuildings = {}

    for id in buildings:
        curr = buildings[id]
        newBuildings[id] = {}
        iterdict(curr, id, id, newBuildings[id])

    with open('../processed_data/NoMorphFlattened.json', 'w') as jsonFile:
        json.dump(newBuildings, jsonFile) 

def main():
    flatten()

if __name__ == '__main__':
    main()