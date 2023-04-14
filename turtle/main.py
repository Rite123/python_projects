import turtle

import random
strange = turtle.Turtle()

screen = turtle.Screen()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand = (r, g, b)
    return rand


# lst = ["cyan","dodger blue","lime","dark red","blue violet","indigo","tomato","cadet blue","magenta","indian red"]
strange.shape("circle")
# strange.pensize(3)
# i=3
# for i in range(3, 11):
#     strange.color(random.choice(lst))
#     for j in range(i):
#         strange.forward(150)
#         strange.right(360/i)
#
# angles=[0,90,180,270]
strange.speed("fastest")
# for i in range(200):
#     strange.color(random_color())
#     strange.forward(50)
#     strange.setheading(random.choice(angles))

# for i in range(1,100):
#     strange.color(random_color())
#     strange.circle(75,360)
#     strange.left(i+5)


def draw_spiro(size):
    for _ in range(int(360/size)):
        strange.color(random_color())
        strange.circle(100)
        strange.setheading(strange.heading()+size)


draw_spiro(5)
screen.exitonclick()