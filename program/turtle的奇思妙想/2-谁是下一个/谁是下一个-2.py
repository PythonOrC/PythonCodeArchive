import turtle
from random import shuffle

screen = turtle.Screen()
screen.title("谁是下一个？")
screen.bgcolor("sky blue")
screen_width, screen_height = 720, 720
screen.setup(screen_width, screen_height)
screen.setworldcoordinates(0, 0, screen_width, screen_height)
pen = turtle.Pen()
pen.hideturtle()


def new_goto(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def name():
    if people:
        n = total - len(people) + 1
        print(n)
        new_goto(unit*n, screen_height - 400)
        pen.color('black')
        pen.dot(90)
        new_goto(unit*n, screen_height - 420)
        pen.color('white')
        pen.write(people.pop(), align='center',
                  font=("FZY3JW.TTF", 24, "bold"))
        if len(people) == 0:
            pen.pencolor('green')
            new_goto(screen_width/2, screen_height - 600)
            pen.write('所有选手已出场!', align='center',
                      font=("FZY3JW.TTF", 50, "bold"))


people = ["阿短", "小可", "绿豆", "小光", "小加"]
total = len(people)
unit = screen_width/(total+1)

# 写标题
pen.color("white")
new_goto(screen_width/2, screen_height-100)
pen.write("谁是下一个？？", align="center", font=("FZY3JW.TTF", 50, "bold"))

# 显示帮助信息
pen.color("yellow")
new_goto(10, screen_height-150)
pen.write("提示：按下空格键抽取下一位出场选手。", font=("FZY3JW.TTF", 20))

# 参与抽签的人
pen.color("white")
new_goto(10, screen_height-200)
pen.write("参与比赛的人有：", font=("FZY3JW.TTF", 30, "bold"))
new_goto(10, screen_height-260)
pen.write(people, font=("FZY3JW.TTF", 24, "bold"))
shuffle(people)


pen.color('black')
new_goto(10, screen_height - 350)
pen.write('出场顺序：', font=('FZY3JW.TTF', 30, 'bold'))

screen.onkey(name, 'space')
screen.listen()
turtle.done()
