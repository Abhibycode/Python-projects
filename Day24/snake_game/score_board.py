from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score = 0
        with open("data.txt", mode="r+") as data:
            self.highscore = int(data.read())
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score = {self.highscore}", align="center", font=('Arial', 20, "bold"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update_score_board()

    def increase_score (self):
        self.score += 1
        self.update_score_board()
