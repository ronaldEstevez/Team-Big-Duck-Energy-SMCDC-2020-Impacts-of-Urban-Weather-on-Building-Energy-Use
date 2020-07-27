# Team-Big-Duck-Energy-SMCDC-2020-Impacts-of-Urban-Weather-on-Building-Energy-Use

### Setting up Git on your computer: 
https://help.github.com/en/github/getting-started-with-github/set-up-git

### Cloning the repository to your computer for the first time
```sh
$ git init
$ git clone https://github.com/ronaldEstevez/Team-Big-Duck-Energy-SMCDC-2020-Impacts-of-Urban-Weather-on-Building-Energy-Use.git
```

### Pulling from master branch to update local code to match repository
```sh
$ git pull origin master
```

### Pushing changes to repository
```sh
$ git add .
$ git commit -m <commit message>
$ git push origin master
```

### Making a new branch (immediately switches to that branch)
```sh
$ git checkout -b <branch name>
```

### Pushing changes to the repository from a new branch
```sh
$ git push -u origin <branch name>
```

### Pushing changes to the repository from an existing branch
```sh
$ git add .
$ git commit -m <'commit message'>
$ git push origin <branch name>
```

### Pulling from a branch to update local code to match repository
```sh
$ git pull origin <branch name>
```

### Switching to a different branch
```sh
$ git checkout <branch name>
```

Description of files (in progress)
### ./scripts
  - contains scripts used to processing weather data, NoMorph.json, and the csv files in bldgenergyuse\4 - Simulate buildings for urban morphologies\analysis
  - fetch.py is a module used to access a locally stored SQLite database containing pertinent weather data from Chicago
  - analyze_daily_weather is a script that produces json files in K, F, and C of standard deviation, variance, max, min, and avg of daily Chicago weather across all pertinent locations
  - minimize_weather.py is a script that extracts pertinent weather locations into a new csv file and into a local SQLite database
  - noMorphFullSend.py outputs weather data to be used in weatherized eui related analysis


### ./scripts/880/
  - contains scripts previously used to process all weather data
  
### ./processed_data
  - annualGasEnergy.csv assumes last three digits of ids in csv files in bldgenergyuse\4 - Simulate buildings for urban morphologies\analysis
    are useless and that first value is annual energy/gas use
  - dailyWeaterStatsK/F/C.json is a json file with standard deviation, variance, max, min, and avg of daily Chicago weather
    - uses the 390 locations surrounding the given buildings 
  - buildings.csv is the data from the Cesium website with coordinates according to building ids
  - building_specific_heat_cool.xlsx has each buildings daily average weather in Farenheit with 65 subtracted
  - nomorph.xlsx is spreadsheet of NoMorph.json data
  - NoMorphEdited.json is NoMoph.json but with blank outputs removed and subcategories as dictionaries for easier computation
  - streamlined_NoMorph.json contains each noMorph building listed with its location, area, annual elec/natural gas use, and closest weather location
  - streamlined_withWeather.json contains same data as streamlined_NoMorph.json along with daily average weather for ~190 buildings

### ./processed_data/880
  - dailyWeather.csv contains Kelvin, Farenheit, and Celsius measurements of daily highs, lows, and averages
  - chi_hi_lo_avg.json contains highs, lows, and avergages of Chicago weather
  - chi_temp.csv contains kelvin measure means of daily highs, lows, and averages
  - chicago_Radial_weather.png is a linear plot of simple low, average, and highs on a radial graph
  - var.json contains standard deviation, variance, max, min, and avg of daily Chicago weather in Kelvin
    - varC and varF do so in Celsius and Farenheit respectively

 
