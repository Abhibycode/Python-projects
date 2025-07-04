import turtle
import random

colors = ["blue", "green", "orange", "grey", "purple", "brown"]

def draw_polygons(s):
    turtle.pensize(5)
    turtle.goto(0, 0)
    length = 75
    for _ in range(s):
        turtle.forward(length)
        turtle.left(360/s)
    turtle.color(random.choice(colors))
sides = range(3, 21)

def run():
    for multiple_side in sides:
        draw_polygons(multiple_side)

run()

turtle.exitonclick()