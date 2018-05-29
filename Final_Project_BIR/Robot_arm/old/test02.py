import sys
import numpy as np
from time import sleep

from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *
logger_init(logging.INFO)

arm = SwiftAPI()
sleep(2.0)

arm.set_position(200, -200, 190, speed = 1500, timeout = 20)
arm.flush_cmd()


while True:
    sleep(1)