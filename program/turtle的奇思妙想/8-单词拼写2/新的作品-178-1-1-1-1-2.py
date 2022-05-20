import turtle
import random
import time

screen = turtle.Screen()
screen_width, screen_height = 600,600
screen.setup(screen_width, screen_height)
screen.bgcolor("dark green")

ans = ''
with open("../9-翻译机/book.txt", 'r') as f:
    file = f.readlines()
    words = {}
    for item in file:
        word_cn, word_en = item.split()
        words[word_cn] = word_en

def random_word(words):
    w_cn = random.choice(list(words.keys()))
    w_en = words[w_cn]
    letter_info = {}
    num = 0
    for i in w_en:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        letter_info[i+str(num)] = [x,y]
        num+=1
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    letter_info[':)'] = [x, y]
    del words[w_cn]
    return w_cn, w_en, letter_info

pen = turtle.Pen()
pen.hideturtle()

def cut(string):
    if string == ':)':
        return string
    else:
        letter = string
        for j in string:
            if j >= '0' and j <= '9':
                letter = letter.replace(j, '')
                return letter

def new_goto(x, y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

def flash_screen(w_cn, letter_info):
    screen.clear()
    screen.bgcolor("dark green")
    screen.tracer(0)
    new_goto(-screen_width//2+10, screen_height//2-30)
    pen.color("white")
    pen.write(w_cn, font=("FZY3JW.TTF", 20))
    new_goto(-screen_width//2+10, screen_height//2-50)
    pen.write(ans, font=("FZY3JW.TTF", 20))
    for i in letter_info.keys():
        x,y = letter_info[i]
        new_goto(x, y)
        pen.color("gold")
        letter = cut(i)
        pen.write(letter, font=("FZY3JW.TTF", 20, "bold"))

w_cn, w_en, letter_info = random_word(words)
flash_screen(w_cn, letter_info)



def if_in(x, y, pos):
    x_in = x >= pos[0] and x <= pos[0]+20
    y_in = y >= pos[1] and y <= pos[1]+20
    return x_in and y_in



def if_right(x,y):
    more = True
    global ans, w_cn, w_en, letter_info
    letters = list(letter_info.keys())
    new_goto(x,y)
    for i in letters:
        letter_pos = letter_info[i]
        if if_in(x,y, letter_pos):
            if i == ':)':
                if ans == w_en:
                    print(f"{w_en}拼为{ans}拼写正确！")
                else:
                    print(f"{w_en} 拼为{ans} 拼写错误！")
                if words:
                    w_cn, w_en, letter_info = random_word(words)
                    flash_screen(w_cn, letter_info)
                    ans = ''
                else:
                    print('测试结束')
                    screen.clear()
                    screen.bgcolor("dark green")
                    new_goto(0, 0)
                    pen.write('测试结束', align='center', font=("FZY3JW.TTF", 40))
                    more = False
            else:
                ans += i[0]
                pen.write("点中")
                time.sleep(0.5)
                pen.undo()
                del letter_info[i]
            if more:
                flash_screen(w_cn, letter_info)
                screen.onclick(if_right)
            



screen.onclick(if_right)

turtle.done()
