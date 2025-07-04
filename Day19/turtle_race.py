import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(800,600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle you want to bet on race?(Enter a color)")
colors = ["blue", "green", "red", "purple", "black"]
y_positions = [0, 100, 200, -100, -200 ]
all_turtle = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -375, y= y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >375:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won!, The {wining_color} is the winner")
            else:
                print(f"You've lost!, The {wining_color} is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()