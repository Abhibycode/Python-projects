from turtle import Turtle


class ScreenComponent(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 290)
        self.pendown()
        self.segment_length = 20
        self.gap_length = 20
        self.y_position = 290
        
    def border(self):
        while self.y_position > -290:
            self.pendown()
            self.goto(x=0, y= self.y_position - self.segment_length)
            self.y_position -= self.segment_length
            self.penup()
            self.goto(x=0, y= self.y_position - self.gap_length)
            self.y_position -= self.gap_length