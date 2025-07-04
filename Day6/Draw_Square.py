def turnright():
    for i in range(3):
        turn_left()

def square():
    turn_left()
    for i in range(4):
        move()
        turnright()
square()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
