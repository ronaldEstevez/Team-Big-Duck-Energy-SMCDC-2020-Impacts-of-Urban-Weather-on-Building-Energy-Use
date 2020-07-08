# Team-Big-Duck-Energy-SMCDC-2020-Impacts-of-Urban-Weather-on-Building-Energy-Use

### ./scripts
  - contains scripts used to processing weather data, NoMorph.json, and the csv files in bldgenergyuse\4 - Simulate buildings for urban morphologies\analysis
  - fetch.py is a module used to access a locally stored SQL database containing all the weather data from Chicago
  
### ./processed_data
  - annualGasEnergy.csv assumes last three digits of ids in csv files in bldgenergyuse\4 - Simulate buildings for urban morphologies\analysis
    are useless and that first value is annual energy/gas use
  - chi_hi_lo_avg.json contains highs, lows, and avergages of Chicago weather
  - chi_temp.csv contains kelvin measure means of daily highs, lows, and averages
  - chicago_Radial_weather.png is a linear plot of simple low, average, and highs on a radial graph
  - nomorph.xlsx is spreadsheet of NoMorph.json data
  - var.json contains standard deviation, variance, max, min, and avg of daily Chicago weather in Kelvin
    - varC and varF do so in Celsius and Farenheit respectively
  - weather.csv contains kelvin, farenheit, and Celsius measurements of daily highs, lows, and averages
 
