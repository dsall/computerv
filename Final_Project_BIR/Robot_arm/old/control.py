#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 10:11:28 2017

@author: dieter
"""

import Board
board = Board.Board()


while 1:
    pot = board.get_pot()
    print(pot)
    if pot < 0.5:
        board.set_led1(True)
        board.set_led2(False)
    if pot > 0.5:
        board.set_led2(True)
        board.set_led1(False)
    
    board.set_servo1(pot)
    
