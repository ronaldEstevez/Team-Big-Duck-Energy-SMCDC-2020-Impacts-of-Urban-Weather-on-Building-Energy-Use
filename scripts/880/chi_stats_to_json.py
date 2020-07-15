'''
Outputs json file of standard deviation, variance, average, minimum,
and maximum in daily chicago weather.
'''

import pandas as pd
import fetch
import json
import threading

data = {}


def analyze(start, end):
    std = var = avg = min = max = 0
    for month in range(start, end):
        for day in range(1, 32):
            curr_day = f"2015-{str(month).zfill(2)}-{str(day).zfill(2)}"
            df = fetch.get_weather(usecols='oid,temp_K', datetime=curr_day)
            if not df.empty:
                std = df['temp_K'].std()
                var = df['temp_K'].var()
                avg = df['temp_K'].mean()
                min = df['temp_K'].min()
                max = df['temp_K'].max()
                data[curr_day] = {
                    'std': std,
                    'var': var,
                    'avg': avg,
                    'min': min,
                    'max': max
                }


def main():
    t1 = threading.Thread(target=analyze(1, 3), name="t1")
    t2 = threading.Thread(target=analyze(3, 5), name="t2")
    t3 = threading.Thread(target=analyze(5, 7), name="t3")
    t4 = threading.Thread(target=analyze(7, 9), name="t4")
    t5 = threading.Thread(target=analyze(9, 11), name="t5")
    t6 = threading.Thread(target=analyze(11, 13), name="t6")

    threads = [t1, t2, t3, t4, t5, t6]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    with open('../../processed_data/880/var.json', 'w') as json_file:
            json.dump(data, json_file)


if __name__ == '__main__':
    main()
