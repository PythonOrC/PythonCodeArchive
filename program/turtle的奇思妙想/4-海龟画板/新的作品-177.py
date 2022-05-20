import turtle
import random
pen = turtle.Pen()
screen = turtle.Screen()
pen.speed(0)
pen.color('blue')
pen.pensize(10)
coords=[]

def new_goto(x,y):
    pen.goto(x,y)
    coords.append((pen.pos()))

pen.ondrag(new_goto)


def replay():
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    pen.pencolor(gen_color())
    pen.penup()
    pen.goto((x,y))
    pen.pendown()
    for coord in coords:
        pen.goto(coord[0]+x, coord[1]+y)


def gen_color():
    color = '#'
    num = [random.choice(list('0123456789abcdef')) for i in range(6)]
    for i in num:
        color += i
    return color


screen.listen()
screen.onkey(replay, 'r')

turtle.done()
