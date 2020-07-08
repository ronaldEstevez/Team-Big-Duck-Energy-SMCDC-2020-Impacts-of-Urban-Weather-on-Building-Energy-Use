'''
Takes daily chicago temp stats in K and produces json files in F and C
'''

import json

def main():
    with open('../processed_data/var.json') as jsonFile:
        toC = json.load(jsonFile)
    with open('../processed_data/var.json') as jsonFile:
        toF = json.load(jsonFile)

    for key in toF:
        for tag in ['std', 'var', 'avg', 'min', 'max']:
            C = toC[key][tag]
            if tag == 'std':
                toF[key][tag] = C * 1.8
            elif tag == 'var':
                toF[key][tag] = C * (1.8**2)
            else:
                toC[key][tag] = C - 273.15
                toF[key][tag] = toC[key][tag] * 1.8 + 32

    with open('../processed_data/varC.json','w') as jsonFile:
        json.dump(toC, jsonFile)
        
    with open('../processed_data/varF.json','w') as jsonFile:
        json.dump(toF, jsonFile)

if __name__ == '__main__':
    main()