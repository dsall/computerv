import Board
import time

board = Board.Board('/dev/ttyACM1', '/dev/ttyACM0')

start = board.get_photo()
light = board.get_photo()

while (light - start) > -0.25:
    light = board.get_photo()
    position = board.get_pot()
    board.set_servo1(position)
    time.sleep(0.05)

board.disconnect()