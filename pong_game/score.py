from turtle import Turtle
FONT=("courier",80,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score=0
        self.r_score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="left", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="right", font=FONT)

    def left_point(self):
        self.l_score+=1


    def right_point(self):
        self.r_score+=1

