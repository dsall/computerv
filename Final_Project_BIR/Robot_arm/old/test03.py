import numpy
import time
from time import sleep

from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *
logger_init(logging.INFO)

arm = SwiftAPI()
sleep(2.0)


speed = 25000
x_values = [200,200] * 20
y_values = [-100,100] * 20
z_values = [150,190] * 20

# arm.set_gripper(True)
# arm.set_gripper(False)



for x,y,z in zip(x_values,y_values,z_values):
    print(x,y)
    arm.set_position(x, y, z, speed = speed, timeout = 20,wait=True)
    time.sleep(1)


