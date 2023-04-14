import time
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time


is_on=True
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


# paddle=Turtle()
# paddle.penup()
# paddle.shape("square")
# paddle.goto(350,0)
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.color("white")

ball=Ball()

pd_L=Paddle((350, 0))
pd_R=Paddle((-350, 0))

screen.listen()

screen.onkey(pd_L.up,"Up")
screen.onkey(pd_L.Down,"Down")
screen.onkey(pd_R.up,"w")
screen.onkey(pd_R.Down,"s")

# creating score class

score = Score()

x = 0.1

while is_on:
    time.sleep(x)
    screen.update()
    ball.start()
    score.update_score()
    y_cor=ball.ycor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if (ball.distance(pd_L) < 50 and ball.xcor() > 320) or (ball.distance(pd_R) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        x -= 0.02
        if x<0:
            x=0
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()
screen.exitonclick()