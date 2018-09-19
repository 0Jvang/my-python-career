from turtle import *

tracer(False)
speed(0)
setup(1400, 700, 0, 0)
colormode(255)
pensize(50)
goto(-750, 380)
seth(-90)

def f():
	fd(1300)
	seth(0)
	fd(6)

r = 95
for i in range(50):
	r += 3
	pencolor((r, 29, 73))
	f()
	lt(90)
	f()
	rt(90)

done()
