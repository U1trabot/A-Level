#Math + Turtle

import turtle, random
turtle.colormode(255)
turtle.speed("fastest")
while True:
    turtle.right(random.randint(-180,180))
    turtle.forward(random.randint(0,40))
    choice = random.randint(1,2)
    if choice == (1):
        turtle.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    elif choice == (2):
        pass
input()