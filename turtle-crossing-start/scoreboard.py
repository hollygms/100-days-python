from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = -1
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.update_score()



    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", move=False, align="center", font=FONT)