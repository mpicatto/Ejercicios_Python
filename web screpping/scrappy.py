# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import requests
from bs4 import BeautifulSoup


r = requests.get("http://www.todosjuntosporlasvarillas.com.ar", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())
#all=soup.find_all("div",{"class":"cities"})
#print(all)
#for item in all:
 #   print(item.find_all("h2")[0].text)
  #  print(item.find_all("p")[0].text)
