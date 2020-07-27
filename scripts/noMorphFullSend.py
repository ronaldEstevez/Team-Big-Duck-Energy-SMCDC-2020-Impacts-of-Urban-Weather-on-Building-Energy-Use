'''
streamLineNoMorph()
    - reduces data in NoMorph.json to the each building's
      annual elec/gas use, location, area, and closest
      weather reading location; outputs json

insertWeather()
    - appends yearly weather averages to streamlined
      noMorph data; output json

makeSpreadSheet():
    - outputs a spreadsheet of daily average building specific
      data minus 65

rougly 160 distinct weather locations for the 318 buildings
'''


import fetch
import json
from math import sqrt
import pandas as pd
import sqlite3
import threading

def K_to_F(temp):
    return (temp - 273) * 1.8 + 32

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

def closestWeather(missing, buildings):
    closest = closestPoint(missing, list(buildings.keys()))
    return buildings[closest]

def accessDB(data, lats, lons):
    def analyze(start, end):
        for month in range(start, end):
            for day in range(1, 32):
                currDay = f"2015-{str(month).zfill(2)}-{str(day).zfill(2)}"
                df = fetch.get_weather(usecols='avg(temp_K), lat, lon', lat=lats, lon=lons, datetime=currDay, groupBy='lat, lon')
                if not df.empty:
                    for _, row in df.iterrows():
                        try:
                            data[(row['lat'], row['lon'])][currDay] = row['avg(temp_K)']
                        except:
                            pass

    threads = []

    for i in range(1, 13, 2):
        threads.append(threading.Thread(target=analyze(i, i+2), name="t" + str(i-2)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return data

def streamLineNoMorph():
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
        temp['Total Electricity [GJ]'] = curr['elec_total']
        temp['Total Gas [GJ]'] = curr['outputs']['end_uses'][-1]['Total End Uses']['Natural Gas [GJ]']
        temp['Heating Electricity [GJ'] = curr['outputs']['end_uses'][0]['Heating']['Natural Gas [GJ]']
        temp['Heating Gas [GJ]'] = curr['outputs']['end_uses'][0]['Heating']['Electricity [GJ]']
        temp['Cooling Electricity [GJ'] = curr['outputs']['end_uses'][1]['Cooling']['Electricity [GJ]']
        temp['Building Location [lat, lon]'] = (curr['lat'], curr['lon'])
        temp['Weather Location Lat'] = curr['weather_loc'][0]
        temp['Weather Location Lon'] = curr['weather_loc'][1]
        endResult[id] = temp.copy()
        del temp

    with open('../processed_data/streamlined_NoMorph.json', 'w') as jsonFile:
        json.dump(endResult, jsonFile)

def insertWeather():
    buildings = {}

    with open('../processed_data/streamlined_NoMorph.json', 'r') as jsonFile:
        buildings = json.load(jsonFile)

    lats = []
    lons = []
    data = {}
    
    for _, v in buildings.items():
        lat = v['Weather Location Lat']
        lon = v['Weather Location Lon']
        lats.append(lat)
        lons.append(lon)
        data[(lat, lon)] = {}

    lats = tuple(set(lats))
    lons = tuple(set(lons))

    data = accessDB(data, lats,lons)

    for id in buildings:
        lat = buildings[id]['Weather Location Lat']
        lon = buildings[id]['Weather Location Lon']

        buildings[id]['Weather'] = data[(lat, lon)]

    with open('../processed_data/streamlined_withWeather.json', 'w') as jsonFile:
        json.dump(buildings, jsonFile)

def makeSpreadSheet():
    with open('../processed_data/streamlined_withWeather.json') as jsonFile:
        buildings = json.load(jsonFile)

    buildingWeather = {}

    existing = {}
    for k, v in buildings.items():
        if v['Weather']:
            existing[(v['Weather Location Lat'], v['Weather Location Lon'])] = v['Weather']
            buildingWeather[k] = v['Weather']

    for k, v in buildings.items():
        if not v['Weather']:
            buildingWeather[k] = closestWeather((v['Weather Location Lat'], v['Weather Location Lon']), existing)
        buildings[k]['Weather'] = buildingWeather[k]
    
    df = pd.DataFrame.from_dict(buildingWeather).sort_index(axis=1)
    df = df.apply(lambda x: K_to_F(x) - 65)
    df.to_excel('../processed_data/building_specific_heat_cool.xlsx', index_label = 'date')

    with open('../processed_data/streamlined_withWeather.json', 'w') as jsonFile:
        json.dump(buildings, jsonFile)

def main():
    streamLineNoMorph()
    insertWeather()
    makeSpreadSheet()

if __name__ == "__main__":
    main()
