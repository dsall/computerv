#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 19:11:31 2018

@author: djibrilsall
"""


import sys, os
from time import sleep

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *

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

swift.set_position(10, 0, 80, speed = 8000, wait = True)


x = 200
y = 220

swift.set_position(x, y, 70, speed = 8000, wait = True)
swift.set_position(x, y, 50, speed = 8000, wait = True)
swift.set_position(x, y, 45, speed = 8000, wait =  True)
swift.set_position(x, y, 70, speed = 8000, wait = True)

swift.set_position(10, 0, 80, speed = 8000, wait = True)




swift.set_buzzer()


while True:
    #print(a)
    sleep(1)
