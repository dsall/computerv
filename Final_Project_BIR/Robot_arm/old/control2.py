import Board
board = Board.Board()

while 1:
    pot = board.get_pot()
    lgt = board.get_photo()

    if pot < 0.5:
        board.set_led1(True)
        board.set_led2(False)
    if pot > 0.5:
        board.set_led2(True)
        board.set_led1(False)
    
    board.set_servo1(pot)
    board.set_servo2(lgt)
    
