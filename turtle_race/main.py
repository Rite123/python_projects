from turtle import Turtle,Screen
import random
is_race_on=False

new = Turtle(shape="turtle")
new.shapesize(2,2)
tim=Turtle(shape="turtle")
tim.shapesize(2,2)
tom=Turtle(shape="turtle")
tom.shapesize(2,2)
jerry=Turtle(shape="turtle")
jerry.shapesize(2,2)
micky=Turtle(shape="turtle")
micky.shapesize(2,2)
jack=Turtle(shape="turtle")
jack.shapesize(2,2)

turtle_list=[new,tim,tom,jerry,micky,jack]

new.color("red")
tim.color("blue")
tom.color("green")
jerry.color("yellow")
micky.color("purple")
jack.color("cyan")

scr=Screen()
scr.setup(width=600,height=500)
user_input = scr.textinput(title="Bet on The Turtle",prompt="which Turtle will win The race? enter colour")
new.penup()
new.goto(x=270,y=-130)
tim.penup()
tim.goto(x=270,y=130)
tom.penup()
tom.goto(x=270,y=-80)
jerry.penup()
jerry.goto(x=270,y=80)
micky.penup()
micky.goto(x=270,y=-30)
jack.penup()
jack.goto(x=270,y=30)

if user_input:
    is_race_on=True

while is_race_on:
    for turtle in turtle_list:
        if not turtle.heading() == 180:
            turtle.setheading(180)
        if turtle.xcor() < -260 and user_input == turtle.pencolor():
            print("Your chosen Turtle wins ,Congratulations")
            is_race_on = False
        else:
            if turtle.xcor() < -260 :
                print(f"you lose The winner Turtle is {turtle.pencolor()}")
                is_race_on= False
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)


scr.exitonclick()