from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 20, "bold"))

    def increase_score (self):
        self.score += 1
        self.update_score_board()

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(f"Game Over..  Your Score: {self.score}", align="center", font=('Arial', 30, "bold"))