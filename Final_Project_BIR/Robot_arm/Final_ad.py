#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:03:49 2018

@author: djibrilsall
"""



import sys, os
from time import sleep
import cv2
import numpy as np
import imutils


sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *
from arm import Arm


#logger_init(logging.VERBOSE)
#logger_init(logging.DEBUG)
logger_init(logging.INFO)


print('setup swift ...')

#swift = SwiftAPI(dev_port = '/dev/ttyACM0')
#swift = SwiftAPI(filters = {'hwid': 'USB VID:PID=2341:0042'})
swift = SwiftAPI() # default by filters: {'hwid': 'USB VID:PID=2341:0042'}

print('sleep 2 sec ...')
sleep(2)

print('device info: ')
print(swift.get_device_info())


swift.flush_cmd() # avoid follow 5 command timeout


swift.flush_cmd()
#come Back Home

def home():
    swift.set_position(10, 0, 80, speed = 9000, wait = True)


def movex(x,y,z):
    swift.set_position(x,y,z+20, speed = 10000, wait = True)
    swift.set_position(x,y,z, speed = 1000, wait = True)
    swift.set_pump(True)
    swift.set_position(x,y,z+10, speed = 10000, wait = True)
    swift.set_position(100,-200,80, speed = 9000, wait = True)
    swift.set_pump(False)


cap = cv2.VideoCapture(1)
cap1 = cv2.VideoCapture(1)

class find:
    def detect_object(self, v, w,a,b,c,d,e,f,z):
        _, frame = v.read(c)
        frame = imutils.resize(frame, width=w)
        lower_color = np.array([a,b,c])
        upper_color = np.array([d,e,f])
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        kernel = np.ones((11,11),np.float32)/225
        mask = cv2.inRange(hsv, lower_color, upper_color)
        mask1 = cv2.inRange(hsv, lower_color, upper_color)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        kernel = np.ones((11,11),np.float32)/225
        red_center = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)[-2]
        center_red = None
        xc = 0
        yc = 0

        if len(red_center) > 0 :
            c = max(red_center, key=cv2.contourArea)
            #((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)

            xc = int(M["m10"] / M["m00"])
            yc = int(M["m01"] / M["m00"])

        self.color = z
        self.xcoord = xc
        self.ycoord = yc
        cv2.imshow("mask", mask1)
    def getcoordx(self):
        return self.xcoord
    def getcoordy(self):
        return self.ycoord
    def getcolor(self):
        return self.color
    def getOuput(self):
        return self.maskoutput

def detect_w_avg(s,w,a,b,c,d,e,f,color):
    i = 0
    xred = 0
    yred = 0
    x = 0,
    y = 0;
    red = find()
    red.detect_object(s, w,a,b,c,d,e,f,color)
    while i < 10:
        xred = xred + red.getcoordx()
        yred = yred + red.getcoordy()
        i += 1
    return (color,(xred/i), (yred/i))



i = 1
while i == 1:
    home()
    sleep(3)
    #color, x,y = detect_w_avg(cap, 600,0,100,100,189,255,255,"red")

    color1, x1,y1 = detect_w_avg(cap, 600,65,60,60,80,255,255,"green")
    color, x,y = detect_w_avg(cap, 600,0,50,50,180,255,255,"brightred")
    print (color, x,y )
    print (color1, x1,y1 )
    movex(80,-20,50)
    sleep(3)
    color1, x1,y1 = detect_w_avg(cap, 600,65,60,60,80,255,255,"green")
    color, x,y = detect_w_avg(cap, 600,0,50,50,180,255,255,"brightred")
    sleep(3)
    print (color, x,y )
    print (color1, x1,y1 )
    i+=1
    #pos=swift.getposition()
    #else:
        #print("No object detected")
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

#i = 0
cv2.destroyAllWindows()
cap.release
