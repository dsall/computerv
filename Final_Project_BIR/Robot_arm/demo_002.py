import numpy

from arm import Arm
from board import Board

a = Arm.connect()
b = Board.connect(verbose=True)

while 1:
    pot = b.get_pot()
    pho = b.get_photo()
    fx = round(numpy.interp(pot, [0, 1], [190, 210]))
    fy = round(numpy.interp(pot, [0, 1], [-200, 200]))
    fz = round(numpy.interp(pot, [0, 0.5, 1], [50, 300, 50]))

    print(pot, fx, fy, fz)
    a.goto(fx, fy, fz, wait=True)
    if pho > 0.8: a.grab(False)
    if pho < 0.8: a.grab(True)
