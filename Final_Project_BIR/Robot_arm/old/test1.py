#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:17:51 2017

@author: dieter
"""

import Board
import time

board = Board.Board('/dev/ttyACM1', '/dev/ttyACM0')
board.set_servo2(0)

##board.calibrate_photo()
#counter = 0
#previous_state = True
#while counter < 10:
#    p = board.get_photo()
#    current_state = False
#    if p > 0.9: current_state = True
#    
#    if previous_state and not current_state:
#        counter = counter + 1
#    print(counter)
#    time.sleep(0.1)
#    previous_state = current_state
#    
#    
#    