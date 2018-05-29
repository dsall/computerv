from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *
import time


def connect():
    return MyArm()


class MyArm():
    def __init__(self, speed=1, logging=False):
        self.speed = speed * 10000
        self.timout = 20
        if logging: logger_init(logging.INFO)
        self.robot = SwiftAPI()
        time.sleep(2)

    def goto(self, x,y,z, wait=False):
        print('goto', x,y,z)
        self.robot.set_position(x, y, z, speed=self.speed, timeout= self.timout, wait= wait, relative=False)

    def step(self, x=None,y=None,z=None, wait=False):
        if x is None: x = 0
        if y is None: y = 0
        if z is None: z = 0
        print('goto', x,y,z)
        self.robot.set_position(x, y, z, speed=self.speed, timeout= self.timout, wait= wait, relative=True)

    def grab(self, value=True):
        self.robot.set_pump(value, self.timout)
