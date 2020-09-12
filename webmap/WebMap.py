# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:00:15 2019

@author: Mauro
"""

import folium #imports library folium to publish maps on leaflet
import pandas #import pandas library
data=pandas.read_csv("volcanoes.txt") #opens text file and store it in a data dictionary
lat=list(data["LAT"]) #create a list from values from data dictionary, LAT key
lon=list(data["LON"]) #create a list from values from data dictionary, LON key
elev=list(data["ELEV"]) #create a list from values from data dictionary, ELEV key

def marker_color(elevation): #defines fuction to color circle marker by elevation
    if elevation < 1000:
        return "green"
    elif 1000<= elevation <3000:
        return "orange"
    else:
        return "red"

map=folium.Map([38.470439, -101.859814],zoom_start=5) #Sets basemap
volcanoes=folium.FeatureGroup(name="US Volcanoes") #creats a feature group for volcanoes
for lt, ln, el in zip (lat,lon,elev): #iterates items trough lat,long and elev listis
    volcanoes.add_child(folium.CircleMarker(location=[lt, ln],radius=5,color=marker_color(el),fill_color=marker_color(el),
                                     fill_opacity=1, popup="%d m."%el)) #add a feature to the feature group volvanoes. A circle marcker locatesd by items in lat and long, coloured by a function using items from elev as argumets and usig them has text inside the popups. 
population=folium.FeatureGroup(name="World Population")#creates a feature group called population
population.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),#adds a polygon layer using a geojson file, and sets  trough a lambda function the colours of the features depending the attributoe. in this case Countrys are coloured by population.
                            style_function=lambda x:{"fillColor":"green" if x ["properties"]["POP2005"] <20000000 
                                                     else "brown" if 20000000<= x["properties"]["POP2005"] <60000000 
                                                     else "yellow" if 60000000 <= x["properties"]["POP2005"] <100000000 
                                                     else "orange" if 100000000 <= x["properties"]["POP2005"] <200000000
                                                     else "blue" if 200000000<= x["properties"]["POP2005"] <600000000
                                                     else "red"}))
  
map.add_child(volcanoes) #adds feature group volcanoes to the map
map.add_child(population) #adds feature group population ton the map   
map.add_child(folium.LayerControl()) #sets a layer control, to turn off and on the layers
map.save("Map1.html") #saves map to an HTML file


