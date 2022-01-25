# %% [code] {"execution":{"iopub.status.busy":"2022-01-24T11:25:14.181985Z","iopub.execute_input":"2022-01-24T11:25:14.182870Z","iopub.status.idle":"2022-01-24T11:25:14.205293Z","shell.execute_reply.started":"2022-01-24T11:25:14.182768Z","shell.execute_reply":"2022-01-24T11:25:14.204635Z"}}
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import math
import pandas as pd
import geopandas as gpd
#from geopy.geocoders import Nominatim            # What you'd normally run
from learntools.geospatial.tools import Nominatim # Just for this exercise

import folium 
from folium import Marker
from folium.plugins import MarkerCluster

from learntools.core import binder
binder.bind(globals())
from learntools.geospatial.ex4 import *

def embed_map(m, file_name):
    from IPython.display import IFrame
    m.save(file_name)
    return IFrame(file_name, width='100%', height='500px')
# Load and preview Starbucks locations in California
starbucks = pd.read_csv("../input/geospatial-learn-course-data/starbucks_locations.csv")
starbucks.head()

# How many rows in each column have missing values?
print(starbucks.isnull().sum())

# View rows with missing locations
rows_with_missing = starbucks[starbucks["City"]=="Berkeley"]
rows_with_missing

# Create the geocoder
geolocator = Nominatim(user_agent="kaggle_learn")

def my_geocoder(row):
     try:
        point = geolocator.geocode(row).point
        return pd.Series({'Latitude': point.latitude, 'Longitude': point.longitude})
     except:
        return None
    
berkeyley_locations = rows_with_missing.apply(lambda x: my_geocoder(x['Address']), axis=1)
starbucks.update(berkeyley_locations)
# Create a base map
m_2 = folium.Map(location=[37.88,-122.26],tiles='openstreetmap', zoom_start=13)

# Your code here: Add a marker for each Berkeley location
for idx, row in starbucks[starbucks["City"]=='Berkeley'].iterrows():
    Marker([row['Latitude'], row['Longitude']], popup=row['Address']).add_to(m_2)
# Show the map
embed_map(m_2, 'q_2.html')

CA_counties = gpd.read_file("../input/geospatial-learn-course-data/CA_county_boundaries/CA_county_boundaries/CA_county_boundaries.shp")
CA_pop = pd.read_csv("../input/geospatial-learn-course-data/CA_county_population.csv", index_col="GEOID")

'''CA_pop contains an estimate of the population of each county.
CA_high_earners contains the number of households with an income of at least $150,000 per year.
CA_median_age contains the median age for each county.'''

# Creating the DatFrames
CA_high_earners = pd.read_csv("../input/geospatial-learn-course-data/CA_county_high_earners.csv", index_col="GEOID")
CA_median_age = pd.read_csv("../input/geospatial-learn-course-data/CA_county_median_age.csv", index_col="GEOID")
cols_to_add = CA_pop.join([CA_high_earners, CA_median_age]).reset_index()
CA_stats = CA_stats = CA_counties.merge(cols_to_add, on="GEOID")

CA_stats["density"] = CA_stats["population"] / CA_stats["area_sqkm"]

'''select counties where:

there are at least 100,000 households making $150,000 per year,
the median age is less than 38.5, and
the density of inhabitants is at least 285 (per square kilometer).
Additionally, selected counties should satisfy at least one of the following criteria:

there are at least 500,000 households making $150,000 per year,
the median age is less than 35.5, or
the density of inhabitants is at least 1400 (per square kilometer).'''
# the code 
sel_counties = CA_stats[((CA_stats.high_earners > 100000) &
               (CA_stats.median_age < 38.5) &
               ((CA_stats.density > 285) &
               (CA_stats.high_earners > 500000)|
               (CA_stats.median_age < 35.5)|
               (CA_stats.density > 1400)))]

#Identifying stores within the counties
starbucks_gdf = gpd.GeoDataFrame(starbucks, geometry=gpd.points_from_xy(starbucks.Longitude, starbucks.Latitude))
starbucks_gdf.crs = {'init': 'epsg:4326'}
'''Number of stores within the counties'''
locations_of_interest = gpd.sjoin(starbucks_gdf, sel_counties)
num_stores = len(locations_of_interest)

# Create a base map
m_6 = folium.Map(location=[37,-120], zoom_start=6)

# Show selected store locations
mc = MarkerCluster()

locations_of_interest = gpd.sjoin(starbucks_gdf, sel_counties)
for idx, row in locations_of_interest.iterrows():
    if not math.isnan(row['Longitude']) and not math.isnan(row['Latitude']):
        mc.add_child(folium.Marker([row['Latitude'], row['Longitude']]))

m_6.add_child(mc)

# Show the map
embed_map(m_6, 'q_6.html')
