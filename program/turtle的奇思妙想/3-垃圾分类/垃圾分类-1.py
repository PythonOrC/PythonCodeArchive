import turtle
import random
from time import sleep

screen = turtle.Screen()
screen.title("垃圾分类")
screen.bgcolor("sky blue")
screen_width, screen_height = 700, 700
screen.setup(screen_width, screen_height)
screen.setworldcoordinates(0, 0, screen_width, screen_height)

pen = turtle.Pen()
pen.hideturtle()
pen.speed(0)

info = turtle.Pen()
info.speed(0)
info.hideturtle()


def new_goto(mypen, x, y):
    mypen.penup()
    mypen.goto(x, y)
    mypen.pendown()


def fading(mypen, label, style='bold', font_size=50, duration=0.5):
    mypen.write(label, align='center',
                font=('FZY3JW.TTF', font_size, style))
    sleep(duration)
    mypen.undo()


def sort(num):
    if samples_text:
        print('start sorting')
        new_goto(info, screen_width // 2, screen_height // 2 - 200)
        if samples_text[0] in garbage_list[labels[num-1]]:
            info.color('green')
            fading(info, '分类正确！')
            samples_text.pop(0)
            pen.undo()
            pen.write(samples_text, font=('FZY3JW.TTF', 15))
        else:
            info.color('red')
            fading(info, '分类错误！')
        print('finished')
    else:
        info.write('垃圾分类结束！', align='center',
                   font=('FZY3JW.TTF', 50, 'bold'))


def option_1():
    sort(1)


def option_2():
    sort(2)


def option_3():
    sort(3)


def option_4():
    sort(4)


labels = ['可回收', '干垃圾', '湿垃圾', '有害垃圾']
lb_colors = ['blue', 'black', 'brown', 'red']
unit = screen_width // len(labels)
garbage_list = {
    "可回收": ["塑料瓶", "食品罐头", "玻璃瓶", "易拉罐", "报纸"],
    "干垃圾": ["餐巾纸", "一次性水杯", "一次性手套", "打火机", "伞"],
    "湿垃圾": ["五谷杂粮", "米面豆制品", "肉", "内脏", "蛋"],
    "有害垃圾": ["充电电池", "日光灯管", "药品", "指甲油", "纽扣电池"]
}
garbage_samples = [random.sample(value, random.randint(0, 2))
                   for value in garbage_list.values()]
samples_text = []
for items in garbage_samples:
    for item in items:
        samples_text.append(item)
        random.shuffle(samples_text)

# 写标题
pen.color("white")
new_goto(pen, screen_width/2, screen_height-100)
pen.write("垃圾分类，人人有责", align="center", font=("FZY3JW.TTF", 50, "bold"))
pen.color('yellow')
new_goto(pen, screen_width//2, screen_height - 150)
pen.write("提示：按下数字键1~4为列表中第一个垃圾选择正确的分类。", align="center", font=("FZY3JW.TTF", 15))

for i in range(4):
    x, y = i * unit, screen_height // 2 - 50
    new_goto(pen, x, y)
    pen.color(lb_colors[i])
    pen.write(labels[i], font=("FZY3JW.TTF", 30))
    new_goto(pen, x+50, y-50)
    pen.write(i+1, font=("FZY3JW.TTF", 30))

pen.color("black")
new_goto(pen, 0, screen_height // 2 + 100)
pen.write("需要分类的垃圾有：", font=("FZY3JW.TTF", 25))

new_goto(pen, 0, screen_height // 2 + 50)
pen.write(samples_text, font=("FZY3JW.TTF", 15))

screen.listen()
screen.onkey(option_1, '1')
screen.onkey(option_2, '2')
screen.onkey(option_3, '3')
screen.onkey(option_4, '4')
print('ready')
turtle.done()
