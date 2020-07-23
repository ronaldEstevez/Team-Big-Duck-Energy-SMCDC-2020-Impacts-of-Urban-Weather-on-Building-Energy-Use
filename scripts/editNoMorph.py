'''
Edit NoMorph.json to make its values
easier to access
'''

import json

def main():
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

if __name__ == '__main__':
    main()