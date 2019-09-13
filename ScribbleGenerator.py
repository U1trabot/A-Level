#Math + Turtle

import turtle, random
turtle.colormode(255)
turtle.speed("fastest")
for i in range(1,random.randint(20,1000),1):
    turtle.right(random.randint(1,180))
    turtle.forward(random.randint(0,40))
    choice = random.randint(1,2)
    if choice == (1):
        turtle.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    elif choice == (2):
        pass
input()