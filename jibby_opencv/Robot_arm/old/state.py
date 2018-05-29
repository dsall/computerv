#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:49:31 2017

@author: dieter
"""

import Board
import time

board = Board.Board('/dev/ttyACM1', '/dev/ttyACM0')
board.set_servo2(0)

previous = board.get_photo()
while True:
    time.sleep(0.1)
    new = board.get_photo()
    if previous - new > 0.05:
        print('change')
        previous = new
    previous = board.get_photo()
    