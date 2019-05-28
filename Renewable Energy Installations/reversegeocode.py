import pandas as pd
import geocoder
import numpy as np
from opencage.geocoder import OpenCageGeocode
from pprint import pprint

key = "1e6e1fb14b7e44d79a6ffb831b87f50f"

geocoder = OpenCageGeocode(key)

data = pd.read_csv("CityofTorontoRenewableEnergyProjectsInstalled.csv")

print(data)

data["LAT"] = ""
data["LNG"] = ""
location_info = " Toronto, Ontario, Canada"

print(data)

'''
for index, row in data.iterrows():
    row[1] = row[1] + location_info
    print(row[1])
'''

for index, row in data.iterrows():
    print(index)
    print(row[1])
    #g = geocoder.google(row[1])
    #print(g.latlng)
    query = row[1] + location_info
    results = geocoder.geocode(query)
    print('%f, %f' % (results[0]['geometry']['lat'], results[0]['geometry']['lng']))
    data.at[index, "LAT"] = results[0]['geometry']['lat']
    data.at[index, "LNG"] = results[0]['geometry']['lng']

print(data)

data.to_csv("withlatlong.csv")