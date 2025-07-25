import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#create object
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.onkey(fun=player.go_up, key="Up")

#Game Loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    scoreboard.update_scoreboard()

    #Detect Collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #start new level
    if player.is_at_finish_line():
        player.go_to_start()