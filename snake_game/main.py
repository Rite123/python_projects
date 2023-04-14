from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time
screen = Screen()

screen.setup(width=600,height=600)
screen.title("**snake Game**")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score=ScoreBoard()
screen.listen()

screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")

is_on=True

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh_food()
        snake.extend()
        score.score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
#         is_on=False
        # score.game_over()
        score.reset()
        snake.reset()

    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 10:
#             is_on = False
            # score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()

