import turtle
from random import randint, choice

meteor = turtle.Pen()
meteor.hideturtle()
meteor.speed(0)


screen = turtle.Screen()
screen.bgpic('合照.gif')
screen.setup(600, 600)

colors = ['red', 'orange', 'yellow', 'green', 'indigo', 'purple']


def draw_meteor(x=0, y=0):
    meteor.pencolor(choice(colors))
    meteor.penup()
    meteor.goto(x, y)
    meteor.pendown()
    meteor.setheading(0)
    length = 1
    while meteor.xcor() < 300:
        meteor.pensize(length)
        meteor.forward(length)
        meteor.right(1)
        length += 1
    meteor.clear()


def meteor_shower(x, y):
    for i in range(randint(3, 7)):
        draw_meteor(randint(-300, 0), randint(200, 300))


screen.onclick(meteor_shower, btn=1)
turtle.done()
