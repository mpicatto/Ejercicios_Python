# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:53:15 2019

@author: Mauro
"""
import cv2
import glob

imgs=glob.glob("*.jpg")
print(imgs)
for image in imgs:
    img=cv2.imread(image,0)
    resized=cv2.resize(img,(100,100))
    cv2.imshow("Hey",resized)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized"+img+".jpg",resized)