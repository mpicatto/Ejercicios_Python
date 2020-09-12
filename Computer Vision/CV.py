# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:53:15 2019

@author: Mauro
"""
import cv2

img=cv2.imread("galaxy.jpg",0)

print (type(img))
print(img)
print(img.shape)
print(img.ndim)

resized=cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized)
cv2.imwrite("Galaxy2.jpg",resized)
cv2.waitKey(0)
cv2.destroyAllwindows()