import turtle
import random

screen = turtle.Screen()
screen_width, screen_height = 600,600
screen.setup(screen_width, screen_height)
screen.bgcolor("dark green")
screen.tracer(0)

with open ("word.txt", 'r', encoding='gbk') as f:
    file = f.readlines()
    words = {}
    for item in file:
        cn, en = item.split()
        words[cn] = en

word_cn = random.choice(list(words.keys()))
word_en = words[word_cn]

pen = turtle.Pen()
pen.hideturtle()

def new_goto(x, y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

new_goto(-screen_width//2+10, screen_height//2-30)
pen.color("white")
pen.write(word_cn, font=("FZY3JW.TTF", 20))
loc = []
for i in word_en:
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    new_goto(x,y)
    pen.color("gold")
    pen.write(i, font=("FZY3JW.TTF", 20, "bold"))
    loc.append([i,[x,y]])

x, y = random.randint(-250, 250), random.randint(-250, 250)
new_goto(x,y)
pen.write(":)", font=("FZY3JW.TTF", 5, "bold"))
loc.append([":)", [x, y]])

x, y = random.randint(-250, 250), random.randint(-250, 250)
new_goto(x,y)
pen.write(":(", font=("FZY3JW.TTF", 5, "bold"))
loc.append([":(", [x, y]])
print(loc)
turtle.done()
