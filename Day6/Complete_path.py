def turnright():
    for i in range(3):
        turn_left()
def move_forward():
    for i in range(9):
        move()

def MakingMove():
    move_forward()
    turn_left()
    move()
    turn_left()
    move_forward()
    turnright()
    move()
    turnright()

def run():
    for i in range(5):
        MakingMove()
        
        
run()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
