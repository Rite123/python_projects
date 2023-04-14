from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",15,"normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.highscore = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0,275)
        self.pendown()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt") as file:
            self.contents =file.read()
        self.write(f"score:{self.count} HighScore:{self.contents}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.count > self.highscore:
            self.highscore = self.count
        self.count=0
        with open("data.txt",mode="w") as file:
            file.write(str(self.highscore))
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER !!", align=ALIGNMENT, font=FONT)

    def score(self):
        self.clear()
        self.count += 1
        self.update_scoreboard()