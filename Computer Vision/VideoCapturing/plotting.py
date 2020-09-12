# -*- coding: utf-8 -*-
from  video_captur import df
from  bokeh.plotting import figure, show, output_file

p=figure(x_axis_type='datetime', height=100, width=500, responsive=True, title="Grafica de Movimientos")

q=p.quad(left=df["Start"],right=df["End"],bottom=0,top=1, color="red")

output_file("graph.html")

show(p)
