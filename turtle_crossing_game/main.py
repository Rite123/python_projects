import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move,"Up")
scoreboard = Scoreboard()
scoreboard.create()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()


    if player.ycor() == 300:
        player.reset()
        scoreboard.update()
        car_manager.increment()

    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on=False


screen.exitonclick()