import turtle as t
import time, random

colorset = ('red','orange','yellow','blue')

def draw_blank():
	t.pu()
	t.fd(5)

def draw_line(bool_):
	draw_blank()
	t.pd() if bool_ else t.pu()
	t.fd(30)
	draw_blank()
	t.right(90)

def draw_digit(digit):
	draw_line(True) if digit in [2,3,4,5,6,8,9] else draw_line(False)
	draw_line(True) if digit in [0,1,3,4,5,6,7,8,9] else draw_line(False)
	draw_line(True) if digit in [0,2,3,5,6,8,9] else draw_line(False)
	draw_line(True) if digit in [0,2,6,8] else draw_line(False)
	t.lt(90)
	draw_line(True) if digit in [0,4,5,6,8,9] else draw_line(False)
	draw_line(True) if digit in [0,2,3,5,6,7,8,9] else draw_line(False)
	draw_line(True) if digit in [0,1,2,3,4,7,8,9] else draw_line(False)
	t.lt(180)
	t.fd(15)

def draw_text(time_):
	for i in time_:
		t.pencolor((random.randint(0,255), 0, random.randint(150,255)))
		if i == ':':
			t.rt(90); t.fd(25); t.lt(90)
			t.write('：', font=("Arial",40,"normal"))
			t.lt(90); t.fd(25); t.rt(90)
			t.fd(60)
		else:
			draw_digit(eval(i))

def main():
	t.clear()
	t.tracer(False)
	t.setup(520,150,850,0)
	t.colormode(255)
	t.bgcolor('black')
	t.speed(0)
	t.pensize(7)
	t.ht()
	t.pu(); t.goto(-220, 0); t.pd()
	time_ = time.strftime('%H:%M:%S', time.localtime())
	draw_text(time_)
	# time.sleep(1)
	# t.clear()
	t.ontimer(main, 1000)

if __name__ == '__main__':
	main()
	t.done()
