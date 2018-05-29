#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 10:58:18 2017

@author: dieter
"""

import Board
import time
import random
board = Board.Board()

correct = 0

for x in range(10):
    a = random.randint(0,10)
    b = random.randint(0,10)
    
    answer = input(str(a) + ' + ' + str(b) + ' = ')
    answer = int(answer)
    if answer == a + b:
        board.set_leds(False, True)
        correct = correct + 1
    else: 
        board.set_leds(True, False)
    proportion = correct/(x + 1)
    board.set_servo1(proportion)
    time.sleep(1)
    board.set_leds(False, False)

board.stop_all()
