import random
import Board
import time
from matplotlib import pyplot

def callibrate(board):
    board.set_leds(True, False)
    while 1:
        pot = board.get_pot()
        if pot > 0.45 and pot < 0.55: break
    board.set_leds(False, True)

def get_response(board):
    base = board.get_photo()
    while 1:
        photo = board.get_photo()
        pot = board.get_pot()
        board.set_servo1(pot)
        if base - photo > 0.2: break
    board.set_servo1(0.5)
    return pot


low = ['thine', 'dale', 'kith','gall', 'gloaming']
high = ['house', 'boy', 'thief', 'evening', 'you']

words = low + high
responses = []

random.shuffle(words)


board = Board.Board()

board.set_leds(False, False)
for x in words:
    callibrate(board)
    time.sleep(0.5)
    response = get_response(board)
    responses.append(response)
    
pyplot.barh(range(0,10), responses)
pyplot.yticks(range(0,10),words)
pyplot.savefig('familiarity.png')