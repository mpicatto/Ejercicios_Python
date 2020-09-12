#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:06:17 2019

@author: root
"""
#Hacer un grafico de Linea.
#importando libreria Bokeh
import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show

#preparando datos para el grafico
df=pandas.read_excel("verlegenhuken.xlsx")
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10

#preparar el achivo de salida
output_file("Termp_&_Pressure.html", title="Excel data",)

#crear la figura
f=figure(plot_width=800,plot_height=600)

#Propiedades del Gáfico

f.title.text="Temperature and Air Pressure"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color="red"
f.yaxis.minor_tick_line_color="red"
f.xaxis.axis_label="Temperature (ºC)"
f.yaxis.axis_label="Pressure (hPa)"
#f.toolbar.active_tap= "pan"
#f.toolbar.active_tap= "wheel_zoom" 
    

#crear grafico de linea
f.circle(df["Temperature"],df["Pressure"], size=0.5)

#"mostrar grafico"
show(f)