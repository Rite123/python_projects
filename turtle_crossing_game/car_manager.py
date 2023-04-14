from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars_list=[]
        self.no=STARTING_MOVE_DISTANCE

    def create(self):
        random_no= random.randint(1,4)
        if random_no==3:
            new_car = Turtle()
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars_list.append(new_car)

    def increment(self):
        self.no += MOVE_INCREMENT

    def move(self):
        for car in self.cars_list:
            car.backward(self.no)

