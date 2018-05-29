#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 01:35:40 2018

@author: djibrilsall
"""

import cv2
import numpy as np

cam=cv2.VideoCapture(0)
n=0

while True:
   # print n
    returnVal,frame=cam.read()

    img=cv2.GaussianBlur(frame, (5,5), 0)
    img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue_lower=np.array([100,150,0],np.uint8) 
    blue_upper=np.array([120,255,255],np.uint8)
    blue=cv2.inRange(img,blue_lower,blue_upper)

    cv2.imshow('img',blue)

    #n=n+1
    key = cv2.waitKey(10) % 0x100
    if key == 27: break #ESC 