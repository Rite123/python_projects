from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.penup()
        self.color("red")
        self.refresh_food()

    def refresh_food(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
