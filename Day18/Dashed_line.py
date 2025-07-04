import turtle

draw = 10
blank = 2

for _ in range(20):
    turtle.penup()
    turtle.forward(blank)
    turtle.pendown()
    turtle.forward(draw)

turtle.exitonclick()