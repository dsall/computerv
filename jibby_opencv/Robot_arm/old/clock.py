
import datetime
import time
import Board

board = Board.Board('/dev/ttyACM1', '/dev/ttyACM0')

while 1:
    now = datetime.datetime.now()
    hour = now.hour/23
    mins = now.minute/59
    secs = now.second/60
    
    if secs%2==0: 
        board.set_led1(True)
        board.set_led2(False)
    else:
        board.set_led2(True)
        board.set_led1(False)
    
    print(secs)
    board.set_servo1(secs)
    board.set_servo2(mins)
    
    time.sleep(0.5)