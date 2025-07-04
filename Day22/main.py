import time
from turtle import Screen
from screen import ScreenComponent
from paddle import Paddle
from ball import Ball
from score import ScoreBoard

#importing modules
screen = Screen()
paddle = Paddle
ball = Ball()
scoreboard = ScoreBoard()
border = ScreenComponent()
border.border()

#screen setup
screen.listen()
screen.setup(800, 600)
screen.bgcolor("white")
screen.tracer(0)

#creating paddles
r_paddle = paddle((350, 0))
l_paddle = paddle((-350, 0))

screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

#Game loop
is_Game_Over = False
while not is_Game_Over:
    #Smooth motion of ball
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Bounce ball back if touches bottom and top surface
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #if ball touches paddle, bounce back
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #scoring for right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #scoring for left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()