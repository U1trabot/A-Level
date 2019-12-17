import turtle
import random
first = float(input("[:"))
second = float(input("[:"))
third = float(input("[:"))
turtle.speed(0)
turtle.colormode(255)
turtle.color(255,255,255)
turtle.bgcolor(0,0,0)
x = 0
while x < first:
    coord = random.choice([[first-random.randint(-200,200),random.randint(-200,200)],[second-random.randint(-200,200),random.randint(-200,200)],[third-random.randint(-200,200),random.randint(-200,200)]])
    turtle.setpos(coord[0],coord[1])
    x+=1
input()
