import turtle
pen = turtle.Pen()
screen = turtle.Screen()
screen.setup(633, 633)
screen.bgpic("bg.gif")

def new_goto(x, y):
    pen.penup()
    pen.goto(x ,y)
    pen.pendown()


def recite_mode(words):
    line = 0
    for word in words:
        word_cn, word_en = word.split()
        new_goto(-300, 250-line*41)
        pen.write(word_cn, False, 'left', font=('Arial', 16, 'normal'))
        new_goto(-150, 250-line*41)
        pen.write(word_en, False, 'left', font=('Arial', 16, 'normal'))
        line += 1


def test_mode(words):
    line = 0
    for word in words:
        word_cn, word_en = word.split()
        new_goto(-300, 250-line*41)
        pen.write(word_cn, False, 'left', font=('Arial', 16, 'normal'))
        new_goto(-150, 250-line*41)
        ans = screen.textinput("英文输入框", word_cn +"的英文是：")
        if ans == word_en:
            pen.write(word_en, False, 'left', font=('Arial', 16, 'normal'))
        else:
            print("wrong")
            pen.pencolor('red')
            pen.write(word_en, False, 'left', font=('Arial', 16, 'bold'))
            pen.pencolor('black')
        line += 1


with open('word.txt', 'r', encoding='gbk') as f:
    words = f.readlines()

recite_mode(words)
mode = screen.textinput("背单词模式","你准备老好了吗？（提示：输入yes开始背单词）")
if mode == "yes":   
    screen.clear()
    screen.bgpic('bg.gif')
    test_mode(words)
turtle.done()
