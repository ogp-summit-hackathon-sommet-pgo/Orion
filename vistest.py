import pandas as pd
import folium
from folium.plugins import HeatMap

folium_map = folium.Map(location=[43.6532, -79.3832],
                        zoom_start=13,
                        tiles="CartoDB dark_matter")
marker = folium.CircleMarker(location=[43.6532, -79.3832])
marker.add_to(folium_map)

surface_data = pd.read_csv("3DMassing_2018_WGS84.csv")

surface_data_head = surface_data


'''
surface_data["MAX_HEIGHT"]
surface_data["LATITUDE"]
surface_data["LONGITUDE]
surface_data["SHAPE_AREA"]
'''

#print(surface_data.head())

#for index, row in surface_data_head.iterrows():
    #folium.CircleMarker(location = (row["LONGITUDE"], row["LATITUDE"]), radius = 1, fill = True).add_to(folium_map)

heat_map_data = surface_data_head[['LONGITUDE', 'LATITUDE', 'SHAPE_AREA']].groupby(['LONGITUDE', 'LATITUDE']).sum().reset_index().values.tolist()

HeatMap(data = heat_map_data, radius = 8, max_zoom = 13).add_to(folium_map)

folium_map.save("toronto.html")