import random
import turtle

def needle():

    x = random.uniform(-400, 400)
    y = random.uniform(-400, 400)
    angle = random.uniform(0, 360)
    pen.color('red')
    pen.up()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.down()
    pen.forward(100)
    y1 = y
    y2 = pen.ycor()
    d = y2 // 200 - y1 // 200
    if (d==1) or (d==-1):
        return 1

def p1(n):
    count = 0
    for i in range(n):
        if (needle()==1):
            count = count + 1
    print(count, n / count)

screen = turtle.Screen()
screen.setup(800,800)
pen = turtle.Pen()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

for i in range(-400, 400, 200):
    pen.up()
    pen.goto(-400, i)
    pen.down()
    pen.goto(400, i)

for i in range(100):
    needle()
for j in range(10):
    p1(100)
turtle.done()
