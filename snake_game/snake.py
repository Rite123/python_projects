from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

     def __init__(self):
         self.segments=[]
         self.create_snakes()

     def create_snakes(self):
         for position in POSITIONS:
             self.add_segment(position)


     def add_segment(self,position):
         snake = Turtle("square")
         snake.shapesize(1)
         snake.penup()
         snake.goto(position)
         snake.color("white")
         self.segments.append(snake)

     def extend(self):
         self.add_segment(self.segments[-1].position())

     def reset(self):
         for seg in self.segments:
             seg.goto(1000,1000)
         self.segments.clear()
         self.create_snakes()

     def move(self):
         for seg in range(len(self.segments)-1,0,-1):
             xcor=self.segments[seg-1].xcor()
             ycor=self.segments[seg-1].ycor()
             self.segments[seg].goto(xcor,ycor)
         self.segments[0].forward(20)

     def Up(self):
         if self.segments[0].heading() != DOWN:
             self.segments[0].setheading(UP)

     def Down(self):
         if self.segments[0].heading() != UP:
             self.segments[0].setheading(DOWN)

     def Right(self):
         if self.segments[0].heading() != LEFT:
             self.segments[0].setheading(RIGHT)

     def Left(self):
         if self.segments[0].heading() != RIGHT:
             self.segments[0].setheading(LEFT)



