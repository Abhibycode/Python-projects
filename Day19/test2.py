import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()  # Optional: Make the turtle icon invisible

# Write some text at the turtle's current position
pen.write("Hello, Turtle Graphics!", align="center", font=("Arial", 16, "normal"))

# Move the turtle to a different position and write again
pen.penup()      # Lift the pen so we don't draw a line while moving
pen.goto(0, -50)
pen.pendown()    # Put the pen down to write
pen.write("This is another message.", align="left", font=("Verdana", 12, "italic"))

screen.exitonclick()