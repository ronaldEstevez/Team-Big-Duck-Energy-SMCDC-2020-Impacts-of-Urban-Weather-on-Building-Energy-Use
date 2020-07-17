'''
Module for extracting data from SQLITE database
'''

import pandas as pd
import sqlite3

m = {
    "jan":1,
    "feb":2,
    "mar":3,
    "apr":4,
    "may":5,
    "jun":6,
    "jul":7,
    "aug":8,
    "sep":9,
    "oct":10,
    "nov":11,
    "dec":12
}
      
def get_weather(usecols='*', lat=None, lon=None, coordinates=[], months=None, datetime=None, groupBy=None):
    '''
    Fetches data pertaining to Chicago 2015

    Keyword arguements:
    usecols -- columns to be extracted; must be passed as a comma separated string
               valid arguments include:
                    oid, time, lat', lon, temp_K, dewpt_K, RH_pct, pres_Pa, RadDir_Wm-2,
                    RadDif_Wm-2, Longwave_Wm-2, ShortwaveNorm_Wm-2, Shortwave_Wm-2, 
                    WindDir_deg, WindSpd_ms-1, RainDpth_mm

    lat - desired latitude coordinate; must be passed with an argument for lon;
          string, float, or list/tuple of strings/floats

    lon - desired longitude coordinate; must be passed with an argument for lon;
          string, float, or list/tuple of strings/floats

    coordinates - list of tuples of desired coordinates; mutually exclusive with lat and lon

    months - desired months; must be passed as list of strings and months must be
             abbreviated by first three letters; mutually exclusive with datetime
             
    datetime - filter by datetime: must be passed in 'YYYY/MM/DD HH:MM' format but
               does not have to be a complete datetime; mutually exclusive with
               months
    '''

    query = f"select {usecols} from 'chicago_weather'"
    opt_query = []

    for coord in [lat, lon]:
        curr_coord = 'lat' if lat==coord else 'lon'
        if coord != None:
            if type(coord) == tuple:
                opt_query.append(f" {curr_coord} in {coord}")
            elif type(coord) == list and type(lon) == list:
                opt_query.append(f" {curr_coord} in {tuple(coord)}")
            else:
                opt_query.append(f" {curr_coord}={coord}")

    if len(coordinates) > 0 and lat == None and lon == None:
        coord_query = ""
        for coord in coordinates:
            coord_query += f" lat={coord[0]} and lon={coord[1]} or"
        opt_query.append(coord_query[:-3])

    if months != None and len(months) > 0:
        for month in months:
            month = month.lower()
            curr_month = "2015-" + ("0"+str(m[month])) if (m[month]<10) else str(m[months])
            opt_query.append(f" time like '{curr_month}%'")
    elif datetime != None:
        opt_query.append(f" time like '{datetime}%'")
    
    if len(opt_query) != 0:
        query += " where"
        for i in range(0, len(opt_query) - 1):
            query += opt_query[i]
            query += " and"
        query += opt_query[-1]
        
    if groupBy != None:
        query += "group by " + groupBy

    conn = sqlite3.connect('../database/database.db')
    df = pd.read_sql_query(query, conn)  
    conn.close()

    return df 
    
