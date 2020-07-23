'''
Output json file of buildings with some importan variables
from NoMorph.json as easier to access keys
'''

import json
import pandas as pd
from math import sqrt

def closestPoint(givenPoint, points):
    x = givenPoint[0]
    y = givenPoint[1]
    distances = list(map(lambda point: sqrt(
        (x-point[0])**2 + (y-point[1])**2), points))
    return points[distances.index(min(distances))]

def getWeatherCoords():
    weatherDF = pd.read_csv('../weather/weather.csv',
                            usecols=['lat', 'lon'], nrows=15*26)
    coordsList = weatherDF[['lat', 'lon']].values.tolist()
    coords = []
    for point in coordsList:
        coords.append((point[0], point[1]))

    coords = list(coords)

    return coords

def streamline():
    buildings = {}
    with open('../processed_data/NoMorphEdited.json', 'r') as jsonFile:
        buildings = json.load(jsonFile)

    buildingsDF = pd.read_csv('../buildings/chi0_90m_coord2bldg_smc.csv')
    coords = getWeatherCoords()
    endResult = {}
    for id in buildings:
        wanted = buildingsDF[buildingsDF.BLDGID == int(id)]
        buildingCoords = (wanted.Lat.values[0], wanted.Lon.values[0])
        buildings[id]['height'] = wanted.MEAN_AVGHT.values[0]
        buildings[id]['lat'] = buildingCoords[0]
        buildings[id]['lon'] = buildingCoords[1]
        buildings[id]['weather_loc'] = closestPoint(buildingCoords, coords)

        temp = {}
        curr = buildings[id]
        temp['Area [m2]'] = curr['area_total']
        temp['Mean Average Height [m]'] = curr['height']
        temp['Electricity [GJ]'] = curr['elec_total']
        temp['Natural Gas [GJ]'] = curr['outputs']['end_uses'][-1]['Total End Uses']['Natural Gas [GJ]']
        temp['Water [m3]'] = curr['outputs']['end_uses'][-1]['Total End Uses']['Water [m3]']
        temp['Lat'] = curr['lat']
        temp['Lon'] = curr['lon']
        temp['Weather Location Lat'] = curr['weather_loc'][0]
        temp['Weather Location Lon'] = curr['weather_loc'][1]
        endResult[id] = temp.copy()
        del temp

    with open('../processed_data/moo_morph.json', 'w') as jsonFile:
        json.dump(endResult, jsonFile)

def main():
    streamline()

if __name__ == '__main__':
    main()