def turn_right():
    for i in range(3):
        turn_left()

def movement():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
   
def run():
    while at_goal() != True:
        movement()
        
run()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
