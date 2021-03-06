'''
Note that the coordinate frame turns as the robot turns. Forward and backback should really
be defined in terms of the robots current position and not world x,y and z. But hey, this
works as a demo.
'''

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

# for the non-pro swift by current firmware,
# you have to specify all arguments for x, y, z and the speed
swift.set_position(220,320 , 100, speed = 1500, timeout = 20)
