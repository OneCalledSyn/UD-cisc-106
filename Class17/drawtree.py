from turtle import *
screen = Screen()
class Tree:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.pen = Turtle()
    self.pen.hideturtle()
    self.pen.penup()
  
  def draw(self):
    self.pen.goto(self.x, self.y)
    self.pen.left(90)
    self.pen.pensize(10)
    self.pen.pencolor("brown")
    self.pen.pendown()
    self.pen.forward(30)
    self.pen.left(90)
    self.pen.penup()
    self.pen.back(50)
    self.pen.pendown()
    self.pen.color('green')
    self.pen.begin_fill()
    self.pen.forward(100)
    self.pen.right(120)
    self.pen.forward(100)
    self.pen.right(120)
    self.pen.forward(100)
    self.pen.end_fill()

screen.tracer(0)
for i in range(5):
  atree = Tree(-160 + 64*i, -100 + 10*(i % 2))
  atree.draw()
screen.tracer(1)