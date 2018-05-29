

import numpy as np
import time
from time import sleep
import cv2
from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *
logger_init(logging.INFO)

SERVO_BOTTOM = 0
SERVO_LEFT = 1
SERVO_RIGHT = 2
SERVO_HAND = 3

arm = SwiftAPI()
sleep(2.0)
position_arr=[]

angles_arr=[]
'''
       Set servo angle, 0 - 180 degrees, this Function will include the manual servo offset.

       Args:
           servo_id: SERVO_BOTTOM, SERVO_LEFT, SERVO_RIGHT, SERVO_HAND
           angle: 0 - 180 degrees
           wait: if True, will block the thread, until get response or timeout

       Returns:
 
          succeed True or failed False
       '''

for _ in range(100):



    rand = np.random.rand(3)
    angles = rand*180

    print ("angles are",angles)

    arm.flush_cmd()
    arm.reset()

    arm.set_servo_angle_speed( SERVO_RIGHT ,angles[0], wait = True, timeout = 100,speed = 5000)

    arm.set_servo_angle_speed( SERVO_BOTTOM ,angles[1], wait = True, timeout = 100,speed = 5000)

    arm.set_servo_angle_speed( SERVO_LEFT ,angles[2] ,  wait = True, timeout = 100,speed = 5000)
    a= arm.get_is_moving()
    print ("the status is",a,"\n")
    pos = arm.get_position() # float array of the format [x, y, z] of the robots current location
    # pixelpostion= get the pixel position here

    print("the position is ", pos ,"\n")
    position_arr.append(pos)
    angles=angles.tolist()
    angles_arr.append(angles) # [right bottom left]
    sleep(2.0)




DAT =  np.row_stack((position_arr , angles_arr))

print("try final ", DAT)

np.savetxt("data1.text", DAT , newline=" \n ",fmt='%s')
