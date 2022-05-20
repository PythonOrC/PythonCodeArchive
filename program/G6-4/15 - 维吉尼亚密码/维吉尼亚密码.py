import turtle
import time

screen = turtle.Screen()
width, height = 864, 864
screen.setup(width, height)
screen.bgpic("bg.gif")
hori_pen = turtle.Pen()
hori_pen.color("yellow")
hori_pen.speed(5)
hori_pen.pensize(3)

verti_pen = turtle.Pen()
verti_pen.color("yellow")
verti_pen.speed(5)
verti_pen.pensize(3)
verti_pen.setheading(-90)


def goto(pen, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


letter = height / 27


def letter_pos(row, col):
    goto(hori_pen, -width / 2, height / 2 - (1.5 + row) * letter)
    goto(verti_pen, -width / 2 + (1.5 + col) * letter, height / 2)
    verti_pen.forward(height)
    hori_pen.forward(width)


plaintext = screen.textinput("明文", "输入你要加密的文字：")
key = screen.textinput("密钥", "输入你的密钥：")

plaintext_len = len(plaintext)
key_len = len(key)
real_key = key * (plaintext_len // key_len) + key[: plaintext_len % key_len]
letters = list("abcdefghijklmnopqrstuvwxyz")
password = []
cipher = ""
for i in range(26):
    l = list(letters[i:] + letters[:i])
    password.append(l)

for i in range(plaintext_len):
    row_index = ord(plaintext[i].upper()) - 65
    col_index = ord(real_key[i].upper()) - 65
    letter_pos(row_index, col_index)
    cipher += password[row_index][col_index]


time.sleep(3)
screen.clear()
pen = turtle.Pen()
pen.hideturtle()
goto(pen, 0, 0)
pen.pencolor("green")
pen.write(cipher, align="center", font=("Arial", 40, "bold"))

turtle.done()
