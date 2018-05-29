#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 01:45:46 2018

@author: djibrilsall
"""

import cv2
import numpy as np

device = cv2.VideoCapture(0)
while True:
    ret, frame = device.read(0)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_range = np.array([100,150,0])
    upper_range = np.array([120,255,255])
    
    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow("Frame", frame)
    
    result = cv2.bitwise_and(frame, frame,mask=mask)
    cv2.imshow("Result", result)
    
    if cv2.waitKey(1) == 27:
        break
device.release()
cv2.destroyAllWindows()