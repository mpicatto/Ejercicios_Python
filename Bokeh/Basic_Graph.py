#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:06:17 2019

@author: root
"""
#Hacer un grafico sencillo.
#importando libreria Bokeh
import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show

#preparando datos para el grafico
df=pandas.read_csv("data.csv")
x= df["x"]
y=df["y"]

#preparar el achivo de salida
output_file("line_from_CSV.html", title="CSV data")

#crear la figura
f=figure()

#crear grafico de linea
f.line(x,y)

#"mostrar grafico"
show(f)