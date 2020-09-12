#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:48:05 2020

@author: root
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')

def home():
    return "Website content goes here!"

if __name__=="__main__":
    app.run(debug=True)
    
    