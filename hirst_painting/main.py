# import colorgram
import turtle
import random
# color = colorgram.extract("image.jpg", 25)
screen=turtle.Screen()
# color_list=[]
screen.colormode(255)
strange=turtle.Turtle()
#
#
# for colors in color:
#     r=colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     rgb=(r,g,b)
#     color_list.append(rgb)
#
# print(color_list)
#
strange.pensize(4)
color_list=[(211, 154, 97), (52, 107, 132), (176, 78, 34), (200, 142, 33), (116, 155, 171), (124, 79, 98), (122, 175, 157), (229, 197, 128), (190, 88, 109), (55, 38, 19), (11, 51, 65), (44, 168, 125), (197, 122, 141), (50, 125, 120), (167, 21, 29), (225, 94, 80), (244, 162, 160), (4, 28, 26), (38, 32, 34), (80, 148, 170), (162, 26, 21)]
i=50

strange.penup()
strange.setheading(225)
strange.forward(250)
strange.setheading(0)
strange.pendown()
strange.hideturtle()
for _ in range(10):
    for j in range(10):
        strange.dot(20,random.choice(color_list))
        strange.penup()
        strange.forward(50)
        strange.pendown()
    strange.penup()
    strange.setheading(90)
    strange.forward(50)
    strange.setheading(180)
    strange.forward(500)
    strange.setheading(0)
    strange.pendown()
# print(strange.setx(0))
# print(strange.sety(50))

screen.exitonclick()
