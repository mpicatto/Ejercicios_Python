#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:52:18 2019

@author: root
"""

import cv2
#import numpy as np
#import time
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
refresh=int(input("Ingrese velocidad de Actualización (segundos): "))
first_frame = None
video=cv2.VideoCapture(0)
count=0
while count <30:
    count=count+1
    print("\r[+]Timer: " + str(count), end="")
    check, frame=video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #gray = cv2.addWeighted(gray, alpha, np.zeros(gray.shape, gray.dtype),0, beta)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    first_frame=gray
#alpha = 50
#beta = 10
timer=0    
while True:
    timer=timer+1
    print("\r[+]Timer: " + str(timer), end="")
    check, frame=video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    #gray2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    gray=cv2.GaussianBlur(gray,(21,21),0)
    
    if timer == refresh*28:
        first_frame = gray
        print(first_frame)
        timer=0
        continue
    
    delta_frame=None
    delta_frame=cv2.absdiff(first_frame,gray,delta_frame)

    threshold=cv2.threshold(delta_frame, 30, 225, cv2.THRESH_BINARY)[1]
    threshold=cv2.dilate(threshold,None, iterations=2)
    
    (cnts,_)=cv2.findContours(threshold.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w, y+h),(0,255,0), 3)
     
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    #cv2.imshow("Baseline",first_frame)
    #cv2.imshow("Captured", gray)
    #cv2.imshow("Delta",delta_frame)
    #cv2.imshow("Threshold Frame", threshold)
    cv2.imshow("ColorFrame",frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()


