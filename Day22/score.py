from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(x=-100, y=200)
        self.write(f"Score: {self.l_score}", align="center", font=("Courier", 10, "normal"))
        self.goto(x=100, y=200)
        self.write(f"Score: {self.r_score}", align="center", font=("Courier", 10, "normal"))
        self.speed(1)

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(f"Score: {self.l_score}", align="center", font=("Courier", 10, "normal"))
        self.goto(x=100, y=200)
        self.write(f"Score: {self.r_score}", align="center", font=("Courier", 10, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()