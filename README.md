# Team-Big-Duck-Energy-SMCDC-2020-Impacts-of-Urban-Weather-on-Building-Energy-Use

## **Abstract**
This work addresses Challenge 3 of the SMC data challenge by leveraging data-driven tools to understand the relationships between our built environment and nature, and how this relationship impacts energy consumption. It presents detailed results to the research questions posed, along with the rationale for the tools used and limitations of the developed solutions.

## **Team Members / Point of Contact**
  - Sammantha Inneo (sinneo@stevens.edu)
  - Daniel Wadler (dwadler@stevens.edu)
  - Jack Schneiderhan (jschnei4@stevens.edu)
  - Ronald Estevez (restevez@stevens.edu)

## **Overview of Files (important directories and summary italicized)**

### *Summary*
  - reliant on data obtained from SMC Data Challenge Sponsors (https://smc-datachallenge.ornl.gov/challenges-2020/challenge-3-2020/)
  - must run minimize_weather.py to produce supplementary weather data from original weather dataset
  - uses the following Python/Jupyter libraries:
    - folium
    - geopandas
    - hbdscan
    - keplergl
    - matplotlib
    - numpy
    - pandas
    - pyproj
    - pysal
    - seaborn
    - scipy
    - SQLAlchemy

### *_./*
  - energy_analysis.ipynb and weather_analysis.ipynb are partial/incomplete Jupyter notebooks of work done for this project
  - fetch.py and minimize_weather.py are supplementary scripts to weather_analysis.ipynb copied from ./scripts
  - config.py includes map configurations used for energy_analysis.ipynb
  - Final_Paper.pdf is research paper submitted as solution to SMC Datachallenge 3

### ./buldings
  - bldgs_ChicagoLoopLi213Merge0204.csv is building data obtained from the City of Chicago's Open Data Portal
  - chi0_90m_coord2bldg_smc.csv is building data obtained from SMC Data Challenge Sponsors (https://smc-datachallenge.ornl.gov/challenges-2020/challenge-3-2020/)

### ./database
  - in .gitignore
  - SQLite databse produced by minimize_weather.py

### *./figures*
  - paper_figures/ contains figures used in final paper
  - other directories contain other interesting visualizations generated throughout the course of our reserach

### ./weather and ./bldgenergyuse
  - in .gitignore
  - contain data obtained from SMC Data Challenge sponsors (https://smc-datachallenge.ornl.gov/challenges-2020/challenge-3-2020/)
  - ./weather contains reduced weather produced by minimize_weather.py

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
  - processed_data from when all 880 weather locations we're being considered

### ./scripts
  - contains scripts used to process data and generally outputs to ./processed_data
  - noteworthy scripts
    - analyze_daily_weather is a script that produces json files in K, F, and C of standard deviation, variance, max, min, and avg of daily Chicago weather across all pertinent locations
    - daily%.ipynb contain timed, visualization of % weather data for specific days in jupyter notebooks
    - fetch.py is a module used to access a locally stored SQLite database containing pertinent weather data from Chicago
    - minimize_weather.py is a script that extracts pertinent weather locations into a new csv file and into a local SQLite database

### ./scripts/880/
  - contains scripts previously used to process weather data from all 880 locations
  
## **Acknowledgements**
The authors would like to acknowledge the Pinnacle Scholar Program at the Stevens Institute of Technology for their support of this work. The authors would
also like to thank Dr. Philip Odonkor for his invaluable mentorship and support of this work. 

Support for DOI 10.13139/ORNLNCCS/1619243 dataset is provided by the U.S. Department of Energy, project SMC2020 under Contract DE-AC05-00OR22725. Project SMC2020 used resources of the Oak Ridge Leadership Computing Facility at Oak Ridge National Laboratory, which is supported by the Office of Science of the U.S. Department of Energy under Contract No. DE-AC05-00OR22725


 
