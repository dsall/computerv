from board import Board
import time

board = Board.connect()

# First control servo 1 with the dial

start = board.get_photo()
light = board.get_photo()
while (light - start) > -0.25:
    light = board.get_photo()
    position = board.get_pot()
    print('Dial position:', position)
    board.set_servo1(position)
    time.sleep(0.1)
print('done')

# Control servo 2 with the light sensor

start = board.get_pot()
position = board.get_pot()

while abs(position - start) < 0.25:
    light = board.get_photo()
    print('Light sensor:', light)
    position = board.get_pot()
    board.set_servo2(light)
    time.sleep(0.1)

print('done')

