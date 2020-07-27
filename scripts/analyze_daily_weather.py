'''
Outputs daily standard deviation, variance,
average, minimum, and maximum of given measurement
from 390 weather sensor locations surrounding
given buildings as json files
'''

import csv
import fetch
import json
import os
import pandas as pd
import sqlite3
import sys
import threading


def weatherToJSON(val):
    data = {}

    def analyze(val, start, end):
        ogVal = val
        if val[-2] == '-':
            val = f'`{val}`'

        std = var = avg = min = max = 0
        conn = sqlite3.connect('../database/database.db')
        for month in range(start, end):
            for day in range(1, 32):
                curr_day = f"2015-{str(month).zfill(2)}-{str(day).zfill(2)}"
                df = fetch.get_weather(usecols=val, datetime=curr_day, conn=conn)
                if not df.empty:
                    std = df[ogVal].std()
                    var = df[ogVal].var()
                    avg = df[ogVal].mean()
                    min = df[ogVal].min()
                    max = df[ogVal].max()
                    data[curr_day] = {
                        'std': std,
                        'var': var,
                        'avg': avg,
                        'min': min,
                        'max': max
                    }
        conn.close()

    threads = []

    for i in range(1, 13, 2):
        threads.append(threading.Thread(target=analyze, args=(val, i, i+2,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    dir = f'../processed_data/{val}_stats/'

    if not os.path.exists(dir):
        os.makedirs(dir)

    with open(dir + val[val.index('_')+1:] + '.json', 'w') as json_file:
        json.dump(data, json_file)


def weatherStatsToCAndF(val):
    dir = f'../processed_data/{val}_stats/'
    with open(dir + 'K.json') as jsonFile:
        toC = json.load(jsonFile)
    with open(dir + 'K.json') as jsonFile:
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

    with open(dir + 'C.json', 'w') as jsonC, open(dir + 'F.json', 'w') as jsonF:
        json.dump(toC, jsonC)
        json.dump(toF, jsonF)


def main():
    val = ''
    try:
        val = sys.argv[1]
    except IndexError as e:
        print(f'{e}: must provide an argument from weather measurements')
        return

    weatherToJSON(val)

    if val[-1] == 'K':
        weatherStatsToCAndF(val)


if __name__ == '__main__':
    main()
