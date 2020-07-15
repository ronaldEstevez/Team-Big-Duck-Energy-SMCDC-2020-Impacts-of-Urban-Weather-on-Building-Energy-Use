# Team-Big-Duck-Energy-SMCDC-2020-Impacts-of-Urban-Weather-on-Building-Energy-Use

### ./scripts
  - contains scripts used to processing weather data, NoMorph.json, and the csv files in bldgenergyuse\4 - Simulate buildings for urban morphologies\analysis
  - fetch.py is a module used to access a locally stored SQLite database containing pertinent weather data from Chicago
  - analyze_daily_weather is a script that produces json files in K, F, and C of standard deviation, variance, max, min, and avg of daily Chicago weather across all pertinent locations
  - minimize_weather.py is a script that extracts pertinent weather locations into a new csv file and into a local SQLite database

### ./scripts/880/
  - contains scripts previously used to process all weather data
  
### ./processed_data
  - annualGasEnergy.csv assumes last three digits of ids in csv files in bldgenergyuse\4 - Simulate buildings for urban morphologies\analysis
    are useless and that first value is annual energy/gas use
  - buildings.csv is the data from the Cesium website with coordinates according to building ids
  - nomorph.xlsx is spreadsheet of NoMorph.json data
  - NoMorphEdited.json is NoMoph.json but with blank outputs removed and subcategories as dictionaries
  - dailyWeaterStatsK/F/C.json is a json file with standard deviation, variance, max, min, and avg of daily Chicago weather
    - uses the 390 locations surrounding the given buildings 

### ./processed_data/880
  - dailyWeather.csv contains kelvin, farenheit, and Celsius measurements of daily highs, lows, and averages
  - chi_hi_lo_avg.json contains highs, lows, and avergages of Chicago weather
  - chi_temp.csv contains kelvin measure means of daily highs, lows, and averages
  - chicago_Radial_weather.png is a linear plot of simple low, average, and highs on a radial graph
  - var.json contains standard deviation, variance, max, min, and avg of daily Chicago weather in Kelvin
    - varC and varF do so in Celsius and Farenheit respectively

 
