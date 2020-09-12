#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:40:22 2019

@author: root
"""

import cv2

capture=cv2.VideoCapture(0)
frame=capture.read()
cv2.imshow("capture", frame)
key=cv2.waitKey(1)
if key == ord('q'):
    cv2.destroyAllWindows()