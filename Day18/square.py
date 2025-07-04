import turtle

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("Drawing square")
screen.bgcolor("white")
screen.screensize(800, 800)

turtle.shape("arrow") # "elephant" is not a standard shape

for _ in range(4): # Loop 4 times for a basic shape
    turtle.forward(100)
    turtle.left(-90)  # Correct angle for a square

screen.exitonclick()