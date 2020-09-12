# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:23:56 2019

@author: Mauro
"""



import glob2
from datetime import datetime



filenames = glob2.glob("*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:       
        with open(filename, "r") as f:
            file.write(f.read() + "\n")