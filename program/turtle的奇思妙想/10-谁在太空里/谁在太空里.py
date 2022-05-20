import requests
import turtle
r_astros = requests.get('http://api.open-notify.org/astros.json').json()
r_iss = requests.get('http://api.open-notify.org/iss-now.json').json()
lat, lon = r_iss['iss_position']['latitude'], r_iss['iss_position']['longitude']

screen = turtle.Screen()
screen.setworldcoordinates(-360, -180, 360, 180)
screen.setup(730, 370)
turtle.screensize(700, 340)
screen.bgpic('map.gif')
screen.register_shape('iss.gif')
pen = turtle.Pen()
pen.shape('iss.gif')
pen.penup()
pen.goto(float(lon), float(lat))
pen.pensize(5)
pen.color('red')
pen.down()


while True:
    r_astros = requests.get('http://api.open-notify.org/astros.json').json()
    r_iss = requests.get('http://api.open-notify.org/iss-now.json').json()
    lat, lon = r_iss['iss_position']['latitude'], r_iss['iss_position']['longitude']
    print(lat, lon)
    pen.goto(float(lon), float(lat))
    screen.exitonclick()

turtle.done()
