# -*- coding: utf-8 -*-
"""
Created on Wed May 29 02:18:25 2019

@author: Mauro
"""
correct="python123"
i=1
name=input("Ingrese su Nombre:")
lastn=input("Ingrese su Apellido:")
password=input("Ingrese su Contraseña:")

while correct != password and i<3:
    password=input("Constraseña incorrecta\ningrese nuevamente la contraseña:")
    i=i+1
    print("Quedan",3-i,"intentos.")
if password==correct:
    print("Hola %s %s, has sido logeado" % (name,lastn))
else:
    print("Ingreso Denegado")