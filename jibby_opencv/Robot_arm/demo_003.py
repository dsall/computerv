'''
Note that the coordinate frame turns as the robot turns. Forward and backback should really
be defined in terms of the robots current position and not world x,y and z. But hey, this 
works as a demo.
'''

from arm import Arm
from control import Control


def move(arm,x, y, z):
    arm.step(x=x,y=y,z=z, wait=True)

def pump(arm, state):
    arm.grab(state)


my_arm = Arm.connect()


move(arm, 189,-85,70)
pump(arm, True)



while True:
    sleep(1)

