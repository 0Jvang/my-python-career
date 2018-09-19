from turtle import*
import random
speed(0)
bgcolor('black')
colors=['red','yellow','green','blue','orange','purple','pink',]

for i in range(10):
    
    
    penup()
    goto(random.randint(-650,650),random.randint(-350,350))
    pendown()
    for i in range(random.randint(3,14)):
        pensize(4)
        pencolor((random.random(),random.random(),random.random()))
        circle(2+i*6,180)
    penup()
    goto(random.randint(-650,650),random.randint(-350,350))
    pendown()
    for i in range(random.randint(5,25)):
        pensize(4)
        pencolor((random.random(),random.random(),random.random()))
        forward(i*5);left(90)
hideturtle()
done()
