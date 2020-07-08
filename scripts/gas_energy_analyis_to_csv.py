'''
Takes top-most value of every csv file in '..\bldgenergyuse\4 - Simulate buildings for urban morphologies\analysis'
and outputs to a csv file; assumes these are annual gas and energy measurements for each building
'''

import os, json
import pandas as pd

def main():
    energyGasValues = {}

    dir = r'..\bldgenergyuse\4 - Simulate buildings for urban morphologies\analysis'
    for subdir in os.listdir(dir):
            if 'DS' not in subdir:
                energyDF = pd.read_csv(os.path.join(dir, subdir, subdir + "energy_gigj.csv"), nrows=2)
                gasDF = pd.read_csv(os.path.join(dir, subdir, subdir + "gas_gigj.csv"), nrows=2)
                energy = energyDF['value'][0]
                gas = gasDF['value'][0]
                energyGasValues[subdir[:-3]] = {'energy_GJ': energy, 'gas_GJ': gas}
    df = pd.DataFrame.from_dict(energyGasValues, orient='index')
    df.to_csv(r'..\processed_data\annualGasEnergy.csv', index_label='bldgid')

if __name__ == '__main__':
    main()
