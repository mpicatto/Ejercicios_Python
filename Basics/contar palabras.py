# -*- coding: utf-8 -*-
"""
Created on Wed May 29 02:18:25 2019

@author: Mauro
"""
myfile=open("fruits.txt")
content=myfile.read()
print(content)
content=content.splitlines()
print(content)
content.sort(key=str.lower)
myfile.close()
print(content)
print(len(content))
for item in content:
        print("palabra:",item,"-->","Cantidad de Letras:",len(item))

