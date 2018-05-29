
import time
import Board
import random



board = Board.Board('/dev/ttyACM1', '/dev/ttyACM0')

print('Start')

x = random.randrange(1,10)
p = board.get_photo()

cheating = False


board.set_led1(False)
board.set_led2(False)

for i in range(0, x):
    board.set_led2(True)  
    new1 = board.get_photo()
    time.sleep(0.5)
    new2 = board.get_photo()
    board.set_led2(False)
    new3 = board.get_photo()
    time.sleep(0.5)
    new4 = board.get_photo()
    new = min([new1, new2, new3, new4])

    if abs(new - p) > 0.1:
        cheating = True
        break
    
if cheating:  print('You cheated')

p = board.get_photo()
board.set_led1(True)
start = time.time()
while not cheating:
    new = board.get_photo()
    if abs(new - p) > 0.1: break
    
end = time.time()
reaction_time = end - start
print(reaction_time)
    
    
    

