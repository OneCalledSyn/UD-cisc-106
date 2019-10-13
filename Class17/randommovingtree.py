from turtle import *
import random

screen = Screen()

class Tree:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.pen = Turtle()
    self.velocity = (random.randint(-3,3), random.randint(-3,3))

  def move(self):
    self.x += self.velocity[0]
    self.y += self.velocity[1]
  
  def draw(self):
    self.pen.penup()
    self.pen.hideturtle()
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

forest = [Tree(-130 + 64*i, -100 + 10*(i % 2)) for i in range(3)]
for j in range(120):
  screen.tracer(0)
  screen.reset()
  for tree in forest:
    tree.move()
    tree.draw()
  screen.tracer(1)