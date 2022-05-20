import turtle

myscreen = turtle.Screen()
myscreen.setworldcoordinates(0, 0, 800, 800)

mypen = turtle.Pen()
mypen.speed(0)

# 绘制旗面
def rectangle(x, y, width, height, color):
    # 设置画笔
    setpen(x, y, color)
    # 开始绘制
    mypen.begin_fill()
    for i in range(2):
        mypen.forward(width)
        mypen.right(90)
        mypen.forward(height)
        mypen.right(90)
    mypen.end_fill()


# 绘制五角星
def starmac(x, y, angle, length, color):
    # 设置画笔
    setpen(x, y, color)
    # 设置画笔朝向
    mypen.setheading(angle)
    # 开始绘制
    mypen.begin_fill()
    for i in range(5):
        mypen.forward(length)
        mypen.left(72)
        mypen.forward(length)
        mypen.right(144)
    mypen.end_fill()


# 设置画笔
def setpen(x, y, color):
    mypen.penup()
    mypen.setheading(0)
    mypen.goto(x, y)
    mypen.pencolor(color)
    mypen.fillcolor(color)
    mypen.pendown()
    # 设置画笔为 0 度
    mypen.setheading(0)


def draw_star(per, mx, my, a, b, c, d, e, flag=True):
    import math
    R = 1 * per
    ox, oy = mx + a * per, my - b * per
    angle = math.degrees(math.atan(c / d))
    oh = R * math.sin(math.radians(angle))
    ah = R * math.cos(math.radians(angle))
    ax, ay = ox - ah, oy - oh
    length = (R - R * math.cos(math.radians(72))) / math.cos(math.radians(18))
    if not flag:
        starmac(ax, ay, -angle + e, length, "yellow")
    else:
        starmac(ax, ay, angle + e, length, "yellow")

# 主程序


def main():
    per = 20
    mx, my = 100, 700
    # 旗面
    width, height = 30 * per, 20 * per
    rectangle(mx, my, width, height, "red")
    # 大五角星
    import math
    R = 3 * per
    ox, oy = mx + 5 * per, my - 5 * per
    fa = R * math.sin(math.radians(72))
    fo = R * math.cos(math.radians(72))
    ax, ay = ox - fa, oy + fo
    length = (R - R * math.cos(math.radians(72))) / math.cos(math.radians(18))
    starmac(ax, ay, 0, length, "yellow")
    draw_star(per, mx, my, 10, 2, 3, 5, 18)
    draw_star(per, mx, my, 12, 4, 1, 7, 18)

    draw_star(per, mx, my, 12, 7, 2, 7, 18,False)
    draw_star(per, mx, my, 10, 9, 4, 5, 18,False)

    # 隐藏画笔
    mypen.hideturtle()
    turtle.done()


main()
