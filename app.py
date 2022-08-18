import folium
import pandas as pd
import numpy as np
# import geopandas as gpd
from pandas_geojson import read_geojson 
import geojson
import geocoder
import geopy
from vega_datasets import data as vds
import ipywidgets
from folium import plugins
import os


# Open the geojson file and load into a variable
with open('C:/Users/djoco/UpWork/Zip_Code_Map/Zip_Codes.geojson') as f:
    gj = geojson.load(f)

# Capture which zipcode you want
feature1 = gj['features'][0]

# Create Zip Code Dictionary with Long and Lats
zip_code = feature1['properties']['ZIP']
longLat = feature1['geometry']['coordinates'][0]
zipDict = {zip_code: longLat}
print(longLat[0][1])


# Find Range to see if circles falls in each range
# if longLat[0][0] > 0:
# 	x = max([sublist[0] for sublist in longLat])
# 	print(x)
# else:
# 	x = min([sublist[0] for sublist in longLat])
# 	print(x)

# lon = feature1['geometry']['coordinates'][0][0][0]
# lat = feature1['geometry']['coordinates'][0][0][1]


# create map object 
mapObj = folium.Map(location=[37.474858084971046, -97.14111328125001],
					zoom_start=5
					)

# 250 mile circle around a certin point (need to swap long and lat positions)
folium.Circle(radius = 201168, location=(longLat[0][1] , longLat[0][0]), color='green').add_to(mapObj)


# SEE IF BOTH LAT AND LONG RANGES FOR BOTH ZIP CODES OVERLAP, (AFTER DRAWING CIRCLE)



# bordersStyle={
# 	'color': 'blue',
# 	'weight': 1,
# 	'fillOpacity': .1
# }

# # folium.GeoJson("Zip_Codes.geojson", 
# # 				name="Zip Codes",
# # 				style_function= lambda x: bordersStyle
# # 				).add_to(mapObj)


mapObj = folium.Map(
location=[42.82995815, -74.78991444],
tiles = 'cartodbpositron',
zoom_start=4
)



# Add Search Bar
obj = folium.GeoJson(gj).add_to(mapObj)
test = plugins.Search(obj, position='topleft', geom_type='Point',placeholder="Search", search_label='ZIP', search_zoom=12, collapsed=False).add_to(mapObj)


# folium.features.Choropleth(gj, fill_color='RuBu', highlight=True).add_to(mapObj)
data = os.path.join('Zip_Codes.geojson')
folium.GeoJson(data, popup=folium.GeoJsonPopup(fields=[str('ZIP').replace(",","")])).add_to(mapObj)

# geo_json = folium.GeoJson(nodeData, popup=folium.GeoJsonPopup(fields=['name']))



mapObj.save('output.html')


# https://docs.mapbox.com/mapbox-gl-js/example/measure/
# https://www.youtube.com/watch?v=h16O4xt6yBU&ab_channel=LearningSoftwareSkills
# https://data.amerigeoss.org/dataset/zip-codes-2360f/resource/3aeb8b59-92d9-43a6-b959-28b7ee324866







# TEXT BOX
# from folium import IFrame
# text = 'your text here'
# iframe = folium.IFrame(text, width=700, height=450)
# popup = folium.Popup(iframe, max_width=3000)
# Text = folium.Marker(location=[lat,lon], popup=popup,
#                      icon=folium.Icon(icon_color='green'))
# Yourmap.add_child(Text)
# Yourmap.save('mymap.html') 