import Board
import time
from matplotlib import pyplot

board = Board.Board()
values = []

for x in range(0,200):
    light = board.get_photo()
    values.append(light)
    time.sleep(0.1)

pyplot.plot(values)
pyplot.xlabel('time step')
pyplot.ylabel('light intensity (norm.)')
pyplot.savefig('light.png')
