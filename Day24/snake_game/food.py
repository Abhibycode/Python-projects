import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("Red")
        self.speed("fastest")
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)