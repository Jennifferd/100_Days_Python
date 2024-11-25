from turtle import Turtle
FONT = ("Arial", 7, "normal")


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()

    def write_state(self, state: str, x: int, y: int):
        self.goto(x, y)
        self.write(state, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
