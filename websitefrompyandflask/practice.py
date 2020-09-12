# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 18:42:42 2019

@author: Mauro
"""
from flask import Flask, render_template #imports Flask class from flask library and the HTML template renderer
app=Flask(__name__)#intance of Flask class trough a variable.

@app.route('/') #route to the webapp
def home():#funtion to make web app
    return render_template("home.html")

@app.route('/about/')
def about():#funtion to make web app
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
    


