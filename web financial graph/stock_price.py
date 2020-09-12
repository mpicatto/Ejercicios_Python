#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:40:39 2019

@author: root
"""
from pandas_datareader import data
import datetime
import yfinance as yf
from bokeh.plotting import figure, show, output_file

def market(c,o):
    if c > o:
        value="Bull"
    elif c < o: 
        value="Bear"
    else:
        value="Equal"
    return value

start=datetime.datetime(2019,12,1)
end=datetime.datetime(2020,3,1)

df=data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end)
df["Status"]=[market(c,o) for c, o in zip(df.Close,df.Open)]
df["Avg_price"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Open-df.Close)

p=figure(x_axis_type="datetime", width=1000, height=300)
p.title.text="Apple"
p.grid.grid_line_alpha=0.65

hours12=12*60*60*1000
p.rect(df.index[df.Status=="Bull"],df.Avg_price[df.Status=="Bull"],hours12,df.Height[df.Status=="Bull"], fill_color="green", line_color="black") 
p.rect(df.index[df.Status=="Bear"],df.Avg_price[df.Status=="Bear"],hours12,df.Height[df.Status=="Bear"], fill_color="red", line_color="black") 
p.rect(df.index[df.Status=="Equal"],df.Avg_price[df.Status=="Equal"],hours12,df.Height[df.Status=="Equal"], fill_color="black", line_color="black") 
output_file("CS.html")
show(p)