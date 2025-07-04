import math
import random
import turtle

#Basic version
# position = 1
turtle.speed("fastest")
turtle.colormode(255)
colors = range(1, 256)
#
# for _ in range(36):
#     turtle.circle(100)
#     turtle.forward(10)
#     turtle.left(10)
#     position += 1
#     turtle.pencolor((random.choice(colors), random.choice(colors), random.choice(colors)))


#Actual Spirograph
def draw_spirograph(size):
    for _ in range(int(360/size)):
        turtle.circle(100)
        turtle.setheading(turtle.heading()+10)
        turtle.pencolor((random.choice(colors), random.choice(colors), random.choice(colors)))

draw_spirograph(2)