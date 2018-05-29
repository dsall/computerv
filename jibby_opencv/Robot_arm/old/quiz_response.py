import time
import Board

duration = 5

board = Board.Board('/dev/ttyACM1', '/dev/ttyACM0')

print('Start')
p = board.get_photo()


board.set_servo1(0)
board.set_led1(True)

started = time.time()

while 1:
    passed = time.time() - started
    norm = passed/duration    
    new = board.get_photo()
    if norm > 1: break
    if abs(new-p) > 0.1: break
    board.set_servo1(norm)
    
    time.sleep(0.25)

if norm > 1:                      
    board.set_led1(False)   
    board.set_led2(True)

    
