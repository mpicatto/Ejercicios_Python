#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:02:19 2019

@author: root
"""

    from bokeh.plotting import figure, output_file, show
    from bokeh.models import Range1d, LinearAxis
    import pandas
     
    ticker = 'AAPL'
    f = open('alphavantage.co.key')
    apikey = f.read().strip()
    f.close()
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
    ticker =input("Symbol:")
    url1 = '&apikey='
    apikey = "JFQ7FD66XQ7EEPLF"
    url2 = '&datatype=csv'
    getstring = url + ticker + url1 + apikey + url2
     
    df = pandas.read_csv(getstring, parse_dates=['timestamp'])
     
    f = figure(plot_width=800, plot_height=500, x_axis_type="datetime")
     
    f.title.text = "Historical daily price " + ticker
    f.title.text_color = "Gray"
    f.title.text_font = "times"
    f.title.text_font_style = "bold"
    f.xaxis.minor_tick_line_color = None
    f.yaxis.minor_tick_line_color = None
    f.xaxis.axis_label = "Date"
    f.yaxis.axis_label = "Price"    
     
    x = df['timestamp']
    o = df['open']
    h = df['high']
    l = df['low']
    c = df['close']
    z = df['volume']
     
    output_file('line_alphavantage.html') 
     
    f.line(x, o, line_color='red', legend='Open') 
    f.line(x, c, line_color='blue', legend='Close')
    f.line(x, h,line_color='pink', legend='High')
    f.line(x, l, line_color='magenta', legend='Low')
    f.legend.location = "top_left"
    f.y_range = Range1d(df['low'].min(), df['high'].max())
    # Second y range
    f.extra_y_ranges = {'vol': Range1d(df['volume'].min(), df['volume'].max())}
    f.line(x, z, line_color='black', legend='Volume', y_range_name='vol')
    f.add_layout(LinearAxis(y_range_name='vol'), 'right')
     
    show(f) 