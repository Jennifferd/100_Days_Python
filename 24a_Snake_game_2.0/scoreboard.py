from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
FILE_PATH = "data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(FILE_PATH, mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_PATH, mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
