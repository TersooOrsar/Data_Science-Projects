# %% [markdown]
# # Introduction
# 
# It can be a troubling time, but we do have hope on the horizon, with the news we get daily about vaccines. Multiple companies are releasing and getting their vaccines approved; we may  soon see a path forward. 
# 
# Using the robust toolset provided by Kaggle, I'll show you how to create an interactive map to track, for each state, the percentage of inhabitants that have been vaccinated against COVID-19.  
# 
# To get started, if you haven't already, make your own copy of this notebook by clicking on the **[Copy and Edit]** button in the top right corner. 
# 
# This notebook is an example of a project that you can create based on what you'd learn from taking Kaggle's [Geospatial Analysis course](https://www.kaggle.com/learn/geospatial-analysis).
# 
# # US Vaccine Tracker
# 
# We'll use two datasets.  
# 
# - The first dataset has the total number of inhabitants of each state, along with latitude and longitude data for each state's capital city.  This dataset is pulled from the 2019 US Census, and I've uploaded it [here](https://www.kaggle.com/peretzcohen/2019-census-us-population-data-by-state).
# - The second dataset contains a recent estimate for the total number of people that have been vaccinated in each state.  This [vaccine dataset](https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/us_state_vaccinations.csv) is drawn from [Our World In Data](https://ourworldindata.org/), who update their vaccine datasets from the CDC quite regularly.  Every time you run this notebook, you'll use the most recent version of their data.
# 
# In the next code cell, we load and preprocess the data.  As output, you'll see the total percent of the population that has been vaccinated in the US, along with a preview of the Pandas DataFrame that we'll use to make the tracker.

# %% [code]
# Imports
import pandas as pd
from datetime import date, timedelta
import folium
from folium import Marker, Circle, Choropleth
from folium.plugins import MarkerCluster, HeatMap
import math
import matplotlib.pyplot as plt
import seaborn as sns

# Population Data
populationData = pd.read_csv('/kaggle/input/2019-census-us-population-data-by-state/2019_Census_US_Population_Data_By_State_Lat_Long.csv')

# Get the most recent date for filtering
freshDate = date.today() - timedelta(days=1)
freshDate = date.strftime(freshDate,"%Y%m%d")
freshDate = freshDate[0:4] + "-" + freshDate[4:6] + "-" + freshDate[6:8]

# Vaccination data, for most recent date
vaccinationData = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv')
vaccinationByLocation = vaccinationData.loc[(vaccinationData.date == freshDate)][["location", "people_vaccinated"]]

# Vaccination and population data
vaccinationAndPopulationByLocation = pd.merge(populationData, vaccinationByLocation, left_on='STATE',right_on='location').drop(columns="location")

# Calculate percentage vaccinated by state
vaccinationAndPopulationByLocation["percent_vaccinated"] = vaccinationAndPopulationByLocation["people_vaccinated"] / vaccinationAndPopulationByLocation["POPESTIMATE2019"]

vaccinationAndPopulationByLocation

# %% [code]
# Calculate the total percent vaccinated in the US
percentageTotal = vaccinationAndPopulationByLocation["people_vaccinated"].sum() / vaccinationAndPopulationByLocation["POPESTIMATE2019"].sum()
print('Percentage Vaccinated in the US: {}%'.format(round(percentageTotal*100, 2))) 

# %% [markdown]
# The next code cell uses the data to create a tracker, with one marker for each state.  You can click on the markers to see the percentage of the population that has been vaccinated.

# %% [code]
# Create the map
v_map = folium.Map(location=[42.32,-71.0589], tiles='cartodbpositron', zoom_start=4) 

# Add points to the map
mc = MarkerCluster()
for idx, row in vaccinationAndPopulationByLocation.iterrows(): 
    if not math.isnan(row['long']) and not math.isnan(row['lat']):
        mc.add_child(Marker(location=[row['lat'], row['long']],
                            tooltip=str(round(row['percent_vaccinated']*100, 2))+"%"))
v_map.add_child(mc)

# Display the map
v_map

# %% [code]
#HeatMap to show density of vaccination in the states
h_map = folium.Map(location=[42.32, -71.0589], tiles='cartodbpositron', zoom_start=4)

#Add the HeatMap
HeatMap(data=vaccinationAndPopulationByLocation[['lat', 'long']], radius= 25).add_to(h_map)

h_map

# %% [markdown]
