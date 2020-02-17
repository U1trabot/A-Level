from turtle import Turtle
from random import randint

yaboi = Turtle()
yaboi.color("green")
yaboi.shape("turtle")
yaboi.penup()
yaboi.goto(-160, 100)
yaboi.pendown()

yaboi2 = Turtle()
yaboi2.color("blue")
yaboi2.shape("turtle")
yaboi2.penup()
yaboi2.goto(-160, 70)
yaboi2.pendown()

yaboi3 = Turtle()
yaboi3.color("red")
yaboi3.shape("turtle")
yaboi3.penup()
yaboi3.goto(-160, 40)
yaboi3.pendown()

yaboi4 = Turtle()
yaboi4.color("yellow")
yaboi4.shape("turtle")
yaboi4.penup()
yaboi4.goto(-160, 10)
yaboi4.pendown()

for movement in range(100):
    yaboi.forward(randint(1,5))
    yaboi2.forward(randint(1,5))
    yaboi3.forward(randint(1,5))
    yaboi4.forward(randint(1,5))

input("Press Enter to close")