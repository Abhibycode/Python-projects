from turtle import Turtle, Screen

from pygame.event import clear

turtle = Turtle()
screen = Screen()

screen.listen()

def move_forward():
    turtle.forward(10)

def clockwise():
    turtle.left(5)

def backwards():
    turtle.left(180)

def anti_clockwise():
    turtle.left(-5)

def clearing_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=anti_clockwise)
screen.onkey(key="c", fun=clearing_screen)

screen.exitonclick()