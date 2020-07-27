'''
Add coordinates to csv file extracted from
https://evenstar.ornl.gov/autobem/chicago/
'''


import pandas as pd

def main():
    usecols = ['BLDGID','SSR','TOPELEV_M','MED_SLOPE','BASEELEV_M','HGT_AGL','ROOFTYPE','AREA_M2','AVGHT_M','MINHT_M','MAXHT_M','BASE_M','LEN','WID','ORIENT8','Shape_Leng','Shape_Area']
    df1 = pd.read_csv('../buildings/bldgs_ChicagoLoopLi213Merge0204.csv',usecols=usecols)
    df1 = df1.sort_values(by ='BLDGID')
    df2 = pd.read_csv('../buildings/chi0_90m_coord2bldg_smc.csv')
    lats = []
    lons = []
    for id in list(df1.BLDGID.values):
        lats.append(df2[df2.BLDGID == id].Lat.values[0])
        lons.append(df2[df2.BLDGID == id].Lon.values[0])

    df1.insert(1, "LAT", lats)
    df1.insert(2, "LON", lons)
    df1.to_csv('../processed_data/buildings.csv', index=False)

if __name__ == "__main__":
    main()
