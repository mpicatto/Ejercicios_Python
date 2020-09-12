# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:00:15 2019

@author: Mauro
"""

import folium
import pandas
data=pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def marker_color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<= elevation <3000:
        return "orange"
    else:
        return "red"

map=folium.Map([38.470439, -101.859814],zoom_start=5)
volcanoes=folium.FeatureGroup(name="US Volcanoes")
for lt, ln, el in zip (lat,lon,elev):
    volcanoes.add_child(folium.CircleMarker(location=[lt, ln],radius=5,color=marker_color(el),fill_color=marker_color(el),
                                     fill_opacity=1, popup="%d m."%el))
population=folium.FeatureGroup(name="World Population")
population.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
                            style_function=lambda x:{"fillColor":"green" if x ["properties"]["POP2005"] <20000000 
                                                     else "brown" if 20000000<= x["properties"]["POP2005"] <60000000 
                                                     else "yellow" if 60000000 <= x["properties"]["POP2005"] <100000000 
                                                     else "orange" if 100000000 <= x["properties"]["POP2005"] <200000000
                                                     else "blue" if 200000000<= x["properties"]["POP2005"] <600000000
                                                     else "red"}))
  
map.add_child(volcanoes)
map.add_child(population)    
map.add_child(folium.LayerControl())
map.save("Map1.html")


