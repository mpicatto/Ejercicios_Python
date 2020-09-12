# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 02:09:48 2019

@author: Mauro
"""

from tkinter import *

window=Tk()
def fromKg():
    gramos=round(float(e1_value.get())*1000,2)
    libras=round(float(e1_value.get())*2.20462, 2)
    onzas=round(float(e1_value.get())*35.274,2)
    t1.delete("1.0",END)
    t1.insert(END,gramos)
    t2.delete("1.0",END)
    t2.insert(END,libras)
    t3.delete("1.0",END)
    t3.insert(END,onzas)
    
def clear():
    e1.delete(first=0, last=100)
    t1.delete("1.0",END)
    t2.delete("1.0",END)
    t3.delete("1.0",END)
    
title=Label(window, text="Conversor de Unidades de Peso")
title.grid(row=0, column=1)

e1_value=DoubleVar()
e1=Entry(window,textvariable=e1_value,borderwidth=1, width=10)
e1.grid(row=1, column=0)
e1_label=Label(window, text="Kilogramos")
e1_label.grid(row=1, column=1)
b1=Button(window, text="Convertir", command=fromKg)
b1.grid(row=1, column=2)

t1_label=Label(window, text="Gramos")
t1_label.grid(row=2, column=0)
t2_label=Label(window, text="Libras")
t2_label.grid(row=2, column=1)
t3_label=Label(window, text="Onzas")
t3_label.grid(row=2, column=2)

t1=Text(window, height=1,borderwidth=1, width=10 )
t1.grid(row=3,column=0)
t2=Text(window, height=1,borderwidth=1, width=10 )
t2.grid(row=3,column=1)
t3=Text(window, height=1,borderwidth=1, width=10 )
t3.grid(row=3,column=2)

b1=Button(window, text="Borrar", command=clear)
b1.grid(row=4, column=2)

window.mainloop()
