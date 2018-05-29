#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:03:49 2018

@author: djibrilsall
"""



import sys, os
from time import sleep

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
    if x > 120:
       z = 40
    elif x < 120:
       z = 50
    swift.set_position(x,y,z+20, speed = 10000, wait = True)
    
    swift.set_position(x,y,z, speed = 1000, wait = True)
    swift.set_pump(True)
   #sleep(3)
    swift.set_position(x,y,z+10, speed = 10000, wait = True)
    swift.set_position(100,-200,80, speed = 9000, wait = True)
   #sleep(5)
    swift.set_pump(False) 
    
    
speed1 = 10000
x = [105
,208
,320
,270
,230
,120
,130
,175
,220
,200]
y = [-5
,25
,92
,98
,98
,80
,170
,170
,170
,200]
i = 0
z = 0


while i<len(x):
    movex(x[i], y[i],z)
   #home()
    print(x[i], y[i])
    i += 1
home()


swift.set_buzzer()


while True:
    #print(a)
    sleep(1)
