# -*- coding: utf-8 -*-
"""
Created on Wed May 29 02:18:25 2019

@author: Mauro
"""
temperatures = [10, -20, -289, 100]

def farenwriter(temperatures,filepath):
    with open(filepath,"w") as farenheit:
        for c in temperatures:
            if c>-273.15:
                f=c*9/5+32
                farenheit.write(str(f)+"\n")
                
farenwriter(temperatures,"farenheit.txt")
                



