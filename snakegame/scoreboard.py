from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)

        self.hideturtle()
        self.update()
    def update(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))
    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()



