import turtle

myPen = turtle.Pen()
memo = {1: 1, 2: 1}
color = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

turtle.bgcolor("grey")


def fib(n):
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


def square(r):
    for i in range(4):
        myPen.forward(r)
        myPen.left(90)


for i in range(7):
    y = 5 * fib(i + 2)
    myPen.color(color[i])
    square(y)
    myPen.circle(y, 90)


turtle.done()
