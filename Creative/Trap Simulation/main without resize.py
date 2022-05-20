import turtle
import sys
import array
import time
import random
import pyaudio
import json
import math

def detectPull():
    THRESHOLD = config['SOUND_THRESHOLD']
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    r = array.array('h')
    
    snd_data = array.array('h', stream.read(CHUNK_SIZE))
    if sys.byteorder == 'big':
        snd_data.byteswap()
    r.extend(snd_data)

    silent = max(snd_data) < THRESHOLD

    if not silent:
        if ADVANCE_INFO:
            return True, max(snd_data)
        else:
            return True, '_'
    else:
        return False, '_'

def route():
    print('routing start')
    a = random.randint(10, 45)
    b = random.randint(0, 80)

    Vx3d = VELOCITY * math.sin(math.radians(a)) * math.cos(math.radians(b))
    Vy3d = VELOCITY * math.sin(math.radians(a)) * math.sin(math.radians(b))
    Vz3d = VELOCITY * math.cos(math.radians(a))
    z3d = 0
    dt = DT
    t = DT
    coords3d=[]
    while z3d >= 0:
        x3d = Vx3d * t
        y3d = Vy3d * t
        z3d = Vz3d * t + 0.5*ACC*(t**2)
        coords3d.append((x3d,y3d,z3d))
        t += dt
    print(t, a,b, Vz3d)
    return coords3d, (a, b)
        

with open('config.json','r') as f:
    config = json.load(f)

WIDTH, HEIGHT = config['SCREENSIZE']
START_Y = config['BACKGROUND_HEIGHT']
VELOCITY = config['TARGET_SPEED']
REMIND = eval(config['REMINDER'])
ADVANCE_INFO = eval(config['ADVANCE_INFO'])
ACC = -abs(config['ACCELERATION'])
DT = 1/30


window = turtle.Screen()
window.bgcolor("light blue")
window.bgpic('background.gif')
window.title("Trap Simulation")
window.setup(width=WIDTH, height=HEIGHT-40-32, startx=0, starty=0)
window.setworldcoordinates(-WIDTH/2, -START_Y, WIDTH/2, HEIGHT-START_Y)
window.register_shape('target.gif')

canvas = window.getcanvas()
canvas.itemconfig(window._bgpic, anchor="s")

target = turtle.Turtle()
target.hideturtle()
target.penup()
target.speed(0)
target.goto(0, 80)
target.shape('target.gif')
target.resizemode('user')
target.turtlesize(5)

data = turtle.Turtle()
data.hideturtle()
data.penup()
data.speed(0)
data.goto((WIDTH/-2)+20, START_Y+25)


notification = turtle.Turtle()
notification.hideturtle()
notification.penup()
notification.speed(0)
notification.goto((-WIDTH/2), HEIGHT-START_Y-15)
if REMIND:
    notification.write('Please read readme.md')


count = 0
used = True

while True:
    if used == True:
        coords3d, angles = route()
        side = random.choice([-1, 1])
        coords2d = [(side * i[1], i[2]) for i in coords3d]
        scales = [i[0] for i in coords3d]
        print(scales)
        used = False
        
    pull, sound_level = detectPull()

    if pull:
        count += 1
        target.showturtle()
        start = time.time()

        for coord in coords2d:
            target.goto((coord[0])*7, (coord[1])*7+100)


        used = True
        target.clear()
        target.goto(0, 100)
        target.hideturtle()
        
        if ADVANCE_INFO:
            data.clear()
            data_list = [f'Count: {count}', f'Sound Level: {sound_level}', f'Horizontal Angle: {angles[1]}°', f'Vertical Angle: {angles[0]}°', f'Speed: {VELOCITY}', f'Flight time: {time.time()-start:.2f}s']
            for i in range(len(data_list)):
                data.goto((-WIDTH/2)+5, i*-12+50-START_Y)
                data.write(data_list[i])
    time.sleep(0.05)

