'''
Creates SQLITE database of Chicago weather data (in current directory)
'''

import pandas as pd
from sqlalchemy import create_engine
import shutil

def main():
    filename = '../../weather/epvars90m_ChiLoopOnly_2015.Loop.csv'

    database = create_engine('sqlite:///full_database.db')
    
    headers = ['oid', 'time', 'lat', 'lon', 'temp_K', 'dewpt_K', 'RH_pct', 'pres_Pa', 'RadDir_Wm-2', ' RadDif_Wm-2', 'Longwave_Wm-2', 'ShortwaveNorm_Wm-2', 'Shortwave_Wm-2', 'WindDir_deg', 'WindSpd_ms-1', 'RainDpth_mm']
    for df in pd.read_csv(filename,usecols=headers, chunksize=880*96): # chunksize represents a 24 hour period
        df.rename(columns={' RadDif_Wm-2':'RadDif_Wm-2'}, inplace=True)
        df.to_sql('chicago_weather', database, if_exists='append')
    shutil.move('./full_database.db', '../../database/full_database.db')

if __name__ == '__main__':
    main()