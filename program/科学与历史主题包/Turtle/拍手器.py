import turtle

myscreen = turtle.Screen()
myscreen.setworldcoordinates(0, 0, 800, 800)
mypen = turtle.Pen()

def draw_line(x, y, angle):
    mypen.penup()
    mypen.goto(x, y)
    mypen.setheading(angle)
    mypen.pencolor('black')
    mypen.pensize(30)
    mypen.pendown()
    mypen.forward(100)
    mypen.setheading(0)
    
def main():
    draw_line(400,300,90)
    for i in range(5):
        draw_line(400,400,(i+1) * 30)
    mypen.hideturtle()
    turtle.done()

main()