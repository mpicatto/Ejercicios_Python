# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 02:08:57 2019

@author: Mauro
"""
from tkinter import *

def km2miles():
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)
    
window=Tk()
b1=Button(window,text="Execute",command=km2miles)
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window, height=5, width=20 )
t1.grid(row=0,column=2)


window.mainloop()


