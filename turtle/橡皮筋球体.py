from turtle import*
speed(0)
bgcolor('black')
sides=6
colors=['red','yellow','green','blue','orange','purple']
for i in range(480):
    pencolor(colors[i%sides])
    forward(i*3/sides+i)
    left(360/sides+1)
    pensize(i*sides/200)
    left(91)
hideturtle()
done()
