'''
Reduces weather dataset to sensors within the area
that contains given buildings

Outputs a new csv file and a SQLite Database
'''

import pandas as pd
import csv, shutil
from sqlalchemy import create_engine

data = {}

def minimizeWeather():
    ogWeather = './weather/epvars90m_ChiLoopOnly_2015.Loop.csv'

    df = pd.read_csv(ogWeather, usecols=['lat', 'lon'], nrows=880)
    df = df[df.index >= 220]
    df = df[df.index <= 880-4*22]

    coordsList = df[['lat', 'lon']].values.tolist()
    coords = []
    j = 1
    for point in coordsList:
        if j > 2 and j <= 17:
            # coords.append((str(point[0]), str(point[1])))
            coords.append(('%.6f' % point[0], '%.6f' % point[1]))
        elif (j-5)%17 == 0:
            j = 0
        j += 1

    coords = set(coords)

    with open(ogWeather, 'r') as inp, open('./weather/weather.csv', 'w') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp)

        writer.writerow(next(reader))

        for row in reader:
            if (row[2].strip(), row[3].strip()) in coords:
                writer.writerow(row)

def createDatabase():
    filename = './weather/weather.csv'

    database = create_engine('sqlite:///database.db')
    
    headers = ['oid', 'time', 'lat', 'lon', 'temp_K', 'dewpt_K', 'RH_pct', 'pres_Pa', 'RadDir_Wm-2', 
               ' RadDif_Wm-2', 'Longwave_Wm-2', 'ShortwaveNorm_Wm-2', 'Shortwave_Wm-2', 'WindDir_deg', 
               'WindSpd_ms-1', 'RainDpth_mm']
    for df in pd.read_csv(filename,usecols=headers, chunksize=880*96): # chunksize used to represent a 24 hour period...now it just works
        df.rename(columns={' RadDif_Wm-2':'RadDif_Wm-2'}, inplace=True)
        df.to_sql('chicago_weather', database, if_exists='append')
    shutil.move('./database.db', './database/database.db')


def main():
    minimizeWeather()
    createDatabase()

if __name__ == '__main__':
    main()
