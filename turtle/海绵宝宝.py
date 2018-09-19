from turtle import *
tracer(False)
setup(width=0.6,height=0.9);speed(0);pensize(2)
#头
penup();goto(-200,200);lt(30);pendown()
fillcolor('#F9F900')
begin_fill()
for i in range(4):
    for j in range(4):
        circle(-44.44,60);circle(44.44,60)
    circle(-44.44,60)
    rt(30)
end_fill()
#腮红
penup();goto(-150,20);pendown();dot(60,'#FF5151')
penup();goto(-160,30);pendown();dot(12,'white')
penup();goto(150,20);pendown();dot(60,'#FF5151')
penup();goto(160,30);pendown();dot(12,'white')
#眼眶
penup();goto(0,40);seth(90);pendown()
fillcolor('white')
begin_fill()
circle(75,180);seth(0);fd(150);seth(90)
circle(-75,180);seth(180);fd(150)
end_fill()
#右眼
seth(90);penup();goto(75,115);pendown();fd(20)
seth(60);penup();goto(112.5,105);pendown();fd(20)
seth(120);penup();goto(37.5,105);pendown();fd(20)
fillcolor('#00CACA')
begin_fill()
penup();goto(45,40);pendown();seth(90);circle(-30,180);seth(180);fd(60)
end_fill()
fillcolor('black')
begin_fill()
goto(55,40);seth(90);circle(-20,180);seth(180);fd(40)
end_fill()
#左眼
seth(90);penup();goto(-75,115);pendown();fd(20)
seth(60);penup();goto(-37.5,105);pendown();fd(20)
seth(120);penup();goto(-112.5,105);pendown();fd(20)
fillcolor('#00CACA')
begin_fill()
penup();goto(-105,40);pendown();seth(90);circle(-30,180);seth(180);fd(60)
end_fill()
fillcolor('black')
begin_fill()
goto(-95,40);seth(90);circle(-20,180);seth(180);fd(40)
end_fill()
#鼻子
penup();goto(-10,-30);pendown()
seth(110)
fillcolor('#F9F900')
begin_fill()
for i in range(30):
    fd(2.8);rt(1)
for i in range(54):
    fd(1);rt(3)
seth(-80)
for i in range(30):
    fd(3);rt(1.1)
pencolor('#F9F900')
goto(-10,-30)
end_fill()
#左法令纹
penup();goto(-19,10);pendown();pencolor('black')
seth(-100)
for i in range(45):
    fd(2);rt(3)
#右法令纹
penup();goto(22,10);pendown()
seth(-80)
for i in range(45):
    fd(2);lt(3)
#嘴
penup();goto(-140,10);pendown()
seth(-45);circle(200,90)
seth(150);fd(15);bk(30)
penup();goto(-140,10);pendown()
seth(30);fd(15);bk(30)
#左牙
penup();goto(-5,-49);pendown()
fillcolor('white')
begin_fill()
seth(-90);fd(30);rt(90);fd(40);rt(90);fd(35);goto(-5,-49)
end_fill()
#右牙
penup();goto(5,-49);pendown()
fillcolor('white')
begin_fill()
seth(-90);fd(30);lt(90);fd(40);lt(90);fd(35);goto(5,-49)
end_fill()

penup();goto(-60,-80);pendown()
seth(0);fd(120)
#左手
penup();goto(-200,-200);pendown();fillcolor('#F9F900')
begin_fill()
seth(-135);fd(20);rt(120);fd(80)#手臂
lt(90);circle(-20,180);lt(90);fd(10)
for i in range(60):
    if i<21:
        fd(1);rt(1)
    elif i<31:
        fd(1);rt(14)
    else:
        fd(1);rt(1)
seth(75);fd(10)
for i in range(65):
    if i<21:
        fd(1);rt(1)
    elif i<31:
        fd(1);rt(14)
    else:
        fd(1);rt(1)
seth(155);circle(9,230);lt(180);circle(-9,230)
seth(335);circle(-21,170);lt(180);circle(20,40);goto(-200,-200)
end_fill()
#右手
penup();goto(200,-200);pendown();fillcolor('#F9F900')
begin_fill()
seth(-45);fd(20);lt(120);fd(80)#手臂
rt(90);circle(20,180);rt(90);fd(10)
for i in range(60):
    if i<21:
        fd(1);lt(1)
    elif i<31:
        fd(1);lt(14)
    else:
        fd(1);lt(1)
seth(105);fd(10)
for i in range(65):
    if i<21:
        fd(1);lt(1)
    elif i<31:
        fd(1);lt(14)
    else:
        fd(1);lt(1)
seth(25);circle(-9,230);lt(180);circle(9,230)
seth(205);circle(21,170);lt(180);circle(-20,40);goto(200,-200)
end_fill()
#衣服
seth(-90)
fd(50);rt(90);fd(400);rt(90);fd(50)
#裤子
seth(-90);fillcolor('#D26900')
begin_fill()
fd(80);lt(90);fd(400);lt(90);fd(45);lt(90);fd(400)
end_fill()
pu();goto(-200,-257.5);seth(0)
pensize(3)
for i in range(4):
    pu();fd(16);pd();fd(80)
#领带
pensize(2)
penup();goto(0,-206);pendown();seth(-145);fillcolor('#FF0000')
begin_fill()
fd(15);seth(-35);fd(15);seth(-115);fd(38);seth(-60);fd(26);seth(0);fd(10)
seth(60);fd(26);seth(115);fd(38);seth(180);fd(5);bk(5);seth(35);fd(15)
seth(145);fd(15);seth(180);fd(5)
end_fill()
#衣领
pu();goto(0,-206);pd()
seth(-145);fd(30);seth(155);fd(50)
pu();goto(5,-206);pd()
seth(-35);fd(30);seth(20);fd(55)

hideturtle()
done()

