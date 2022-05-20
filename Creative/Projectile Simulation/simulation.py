import turtle
import numpy as np
import math

screen = turtle.Screen()
screen.setup(600,400)
screen.setworldcoordinates(0,0,600,400)
pen = turtle.Pen()
pen.pendown()
pen.hideturtle()
v = 80
theta = math.radians(80)
g=9.8
t=5
counter = 0
t = np.linspace(0, 50, num=200*t)
for k in t:
    # get positions 
    x = ((v*k)*np.cos(theta)) 
    y = ((v*k)*np.sin(theta))-((0.5*g)*(k**2))
    if y>=0:
        pen.goto(x,y)
    elif y < 0:
        if counter == 2:
            pen.pendown()
            pen.goto(x,y)
            pen.penup()
            counter = 0
        else:
            pen.penup()
            pen.goto(x,y)
        counter+=1
            

turtle.done()