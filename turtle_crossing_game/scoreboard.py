FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count=0
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.color("black")
        self.pendown()

    def create(self):
        self.write(f"LEVEL:{self.count}", align="left", font=FONT)

    def update(self):
        self.clear()
        self.count += 1
        self.create()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write("GAME OVER",align="center",font=FONT)

