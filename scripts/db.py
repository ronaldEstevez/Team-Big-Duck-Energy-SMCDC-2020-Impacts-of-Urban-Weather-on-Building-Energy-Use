'''
Creates SQLITE database of Chicago weather data
'''

import pandas as pd
from sqlalchemy import create_engine

def main():
    file = '../weather/epvars90m_ChiLoopOnly_2015.Loop.csv'

    database = create_engine('sqlite:///database.db')
    
    headers = ['oid', 'time', 'lat', 'lon', 'temp_K', 'dewpt_K', 'RH_pct', 'pres_Pa', 'RadDir_Wm-2', ' RadDif_Wm-2', 'Longwave_Wm-2', 'ShortwaveNorm_Wm-2', 'Shortwave_Wm-2', 'WindDir_deg', 'WindSpd_ms-1', 'RainDpth_mm']
    for df in pd.read_csv(file,usecols=headers, chunksize=880*96): # chunksize represents a 24 hour period
        df.rename(columns={' RadDif_Wm-2':'RadDif_Wm-2'}, inplace=True)
        df['time'] = df['time'].apply(lambda x: pd.Timestamp(x[:10] + ' ' + x[11:]))
        df.to_sql('chicago_weather', database, if_exists='append')

if __name__ == '__main__':
    main()