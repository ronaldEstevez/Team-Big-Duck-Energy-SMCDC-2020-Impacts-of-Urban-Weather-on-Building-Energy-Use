'''
Script to replicate Sam's 'working_nomorph.xlsx' spreadsheet
'''


import editNoMorph
from os import path
import pandas as pd


def main():
    # Check if NoMorphFlattened.json exists and if not create it
    if not path.exists('../processed_data/NoMorphFlattened.json'):
        editNoMorph.flatten()

    # Obtain annual building energy use data
    # Remove columns with only 0 values
    noMorph = pd.read_json('../processed_data/NoMorphFlattened.json', orient='index').sort_index()
    noMorph.index.name = 'BLDGID'
    noMorph = noMorph.loc[:, (noMorph!=0).any(axis=0)]

    # Obtain building footprint areas and heights
    # Remove duplicated entries by area
    footprint_heights = pd.read_csv('../buildings/bldgs_ChicagoLoopLi213Merge0204.csv', usecols=['BLDGID', 'AREA_M2', 'AVGHT_M'], index_col='BLDGID').sort_index()
    footprint_heights = footprint_heights.drop_duplicates('AREA_M2')

    # Merge energy data with building data
    # Rename area and height variables
    # Change index to Adjusted BLDGID values (sequentially index noMorph by BLDGID from least to greatest)
    noMorph = noMorph.merge(footprint_heights, on='BLDGID', how='left', left_index=False, right_index=False)
    noMorph.rename(columns={'AREA_M2':'Shape Area [m2]', 'AVGHT_M':'Height [m]'}, inplace=True)
    noMorph['BLGID'] = noMorph.index
    noMorph.reset_index(inplace=True)

    # Append needed columns to noMorph dataframe
    noMorph['Volume [m3]'] = noMorph['Shape Area [m2]'] * noMorph['Height [m]']
    noMorph['Electricity Intensity/Height (Per Volume)  [MJ/m3]'] = noMorph['Total Electricity Intensity [MJ/m2]']/noMorph['Height [m]'] 
    noMorph['Natural Gas Intensity/Height (Per Volume)  [MJ/m3]'] = noMorph['Total Natural Gas Intensity [MJ/m2]']/noMorph['Height [m]'] 
    noMorph['Net Heating [GJ]'] = noMorph['Heating Electricity [GJ]'] + noMorph['Heating Natural Gas [GJ]']
    noMorph['Net Cooling [GJ]'] = noMorph['Cooling Electricity [GJ]']
    noMorph['Net Cooling + Fans [GJ]'] = noMorph['Net Cooling [GJ]'] + noMorph['Fans Electricity [GJ]']
    noMorph['Heating + Cooling [GJ]'] = noMorph['Net Heating [GJ]'] + noMorph['Net Cooling [GJ]']
    noMorph['Heating + Cooling + Fans [GJ]'] = noMorph['Heating + Cooling [GJ]'] + noMorph['Fans Electricity [GJ]']
    noMorph['Net Heating + Fans [GJ]'] = noMorph['Net Heating [GJ]'] + noMorph['Fans Electricity [GJ]']
    noMorph['% Heating (Heating and Cooling Only)'] = noMorph['Net Heating [GJ]']/noMorph['Heating + Cooling [GJ]'] 
    noMorph['% Cooling (Heating and Cooling Only)'] = noMorph['Net Cooling [GJ]']/noMorph['Heating + Cooling [GJ]']
    noMorph['% Heating (All Energy Use)'] = noMorph['Net Heating [GJ]']/(noMorph['Total End Uses Electricity [GJ]'] + noMorph['Total End Uses Natural Gas [GJ]'])
    noMorph['% Cooling + Fans (All Energy Use)'] = noMorph['Net Cooling + Fans [GJ]']/(noMorph['Total End Uses Electricity [GJ]'] + noMorph['Total End Uses Natural Gas [GJ]'])
    noMorph['% Cooling + Fans (Heating Cooling, and Fans Only)'] = noMorph['Net Cooling + Fans [GJ]']/(noMorph['Heating + Cooling + Fans [GJ]'])
    noMorph['% Heating (Heating Cooling, and Fans Only)'] = noMorph['Net Heating [GJ]']/noMorph['Heating + Cooling + Fans [GJ]']

    noMorph['Ratio Heating/Cooling'] = noMorph['Net Heating [GJ]']/noMorph['Net Cooling [GJ]']

    noMorph.to_excel('../processed_data/fullNoMorph.xlsx',index=False)

if __name__ == '__main__':
    main()
