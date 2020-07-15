'''
Used to add Celsius and Fahrenheit columnns to chi_temp.csv
Outputs a new csv
'''

import pandas as pd

def main():
    df = pd.read_csv("../../proccesed_data/880/chi_temp.csv")

    for tag in ['high', 'low', 'avg']:
        df.rename(columns={tag:f'{tag}_K'}, inplace=True)
        df[f'{tag}_C'] = df[f'{tag}_K'].apply(lambda x: x - 273.15)
        df[f'{tag}_F'] = df[f'{tag}_C'].apply(lambda x: x*1.8 + 32)
    
    df.to_csv("../../processed_data/880/dailyWeather.csv")

if __name__ == "__main__":
    main()