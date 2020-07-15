'''
Outputs json file of daily Chicago high, low, and averarage temperatures
Processes all 880 locations to find measurements
'''

import pandas as pd
import fetch
import json

def main():
    data = {}
    high = low = avg = 0

    for month in range(1, 13):
        for day in range(1,32):
            curr_day = f"2015-{str(month).zfill(2)}-{str(day).zfill(2)}"
            df = fetch.get_weather(usecols='oid,temp_K', datetime=curr_day)
            if not df.empty:
                high = df['temp_K'].max()
                low = df['temp_K'].min()
                avg = df['temp_K'].mean()
                data[curr_day] = {
                    'high': high,
                    'low': low,
                    'avg': avg
                }
    with open('../../processed_data/880/chi_hi_lo_avg.json', 'w') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    main()