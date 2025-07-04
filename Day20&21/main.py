from turtle import Screen
from snake import Snake
from food import Food
import time
from score_board import Scoreboard

#Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Creating object for different classes from different modules imported
is_game_on = True
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 370 or snake.head.xcor() < -370 or snake.head.ycor() > 370 or snake.head.ycor() < -370:
        is_game_on = False
        score.game_over()

    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 5:
            is_game_on = False
            score.game_over()

screen.exitonclick()