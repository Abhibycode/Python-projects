def turn_right():
    for i in range(3):
        turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
        
def run():
    while at_goal() != True:
        if front_is_clear():
            move()
        else:
            jump()

run()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
