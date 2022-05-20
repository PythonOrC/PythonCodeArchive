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
    if  PRACTICE_MODE:
        return True, 'Practice Mode'
    elif not silent:
        return True, max(snd_data)
    else:
        return False, '_'

def route():
    if PRACTICE_MODE:
        a, b =random.choice([[75, -80], [45, -45], [45, 0], [45, 45], [75, 80]])
    else:
        a = random.randint(20,50) * random.choice([-1,1])
        b = random.randint(-80, 80)

    Vx3d = VELOCITY * math.sin(math.radians(a)) * math.cos(math.radians(b))
    Vy3d = VELOCITY * math.sin(math.radians(a)) * math.sin(math.radians(b))
    Vz3d = VELOCITY * math.cos(math.radians(a))
    z3d = 0
    x3d=0
    dt = DT
    t = DT
    coords3d=[]
    upward = True
    while z3d >= x3d/6.5 or upward:
        upward = z3d < x3d/6.5
        x3d = Vx3d * t
        y3d = Vy3d * t
        z3d = Vz3d * t + 0.5*ACC*(t**2)
        coords3d.append((x3d,y3d,z3d))
        t += dt
    return coords3d, (a, b), t

def countdown(seconds):
    for i in range(seconds,0,-1):
        timeIndication.write(str(i), align = 'center', font=('arial',20,'normal'))
        time.sleep(1)
        timeIndication.clear()
        

with open('config.json','r') as f:
    config = json.load(f)

WIDTH, HEIGHT = config['SCREENSIZE']
START_Y = config['BACKGROUND_HEIGHT']
VELOCITY = config['TARGET_SPEED']
REMIND = eval(config['REMINDER'])
ADVANCE_INFO = eval(config['ADVANCE_INFO'])
ACC = -abs(config['ACCELERATION'])
MULTIPLIER = config['MULTIPLIER']
PRACTICE_MODE = eval(config['PRACTICE_MODE'])
DT = 1/30


window = turtle.Screen()
window.bgcolor("light blue")
window.bgpic('background.gif')
window.title("Trap Simulation")
window.setup(width=WIDTH, height=HEIGHT-40-32, startx=0, starty=0)
window.setworldcoordinates(-WIDTH/2, -START_Y, WIDTH/2, HEIGHT-START_Y)
for i in range(101):
    window.register_shape(f'image/{i}.gif')

canvas = window.getcanvas()
canvas.itemconfig(window._bgpic, anchor="s")

target = turtle.Turtle()
target.hideturtle()
target.penup()
target.speed(0)
target.goto(0, 80)

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

timeIndication = turtle.Turtle()
timeIndication.hideturtle()
timeIndication.penup()
timeIndication.speed(0)
timeIndication.goto(5,120)
timeIndication.color('white')


count = 0
used = True

while True:
    
    if used == True:
        coords3d, angles, t = route()
        coords2d = [(i[1], i[2]) for i in coords3d]
        scales = [i[0] for i in coords3d]
        print(scales)
        used = False

    if PRACTICE_MODE:
        countdown(3)

    pull, sound_level = detectPull()

    if pull:
        count += 1
        target.showturtle()
        start = time.time()

        for i in range(len(scales)):
            if target.pos()[0] > -WIDTH/2 and target.pos()[0] < WIDTH/2 and target.pos()[1] <  HEIGHT-START_Y:
                if scales[i]>100:
                    target.shape(f'image/100.gif')
                else:
                    target.shape(f'image/{round(scales[i])}.gif')
                target.goto((coords2d[i][0])*MULTIPLIER, (coords2d[i][1])*MULTIPLIER+100)
                time.sleep(0)


        used = True
        time.sleep(0.2)
        target.clear()
        target.goto(0, 100)
        target.hideturtle()
        
        if ADVANCE_INFO:
            data.clear()
            data_list = [f'Count: {count}', f'Sound Level: {sound_level}', f'Horizontal Angle: {angles[1]}°', f'Vertical Angle: {angles[0]}°', f'Speed: {VELOCITY}', f'Flight time: {time.time()-start:.2f}s | Predicted Flight time: {t:.2f}s']
            for i in range(len(data_list)):
                data.goto((-WIDTH/2)+5, i*-12+62-START_Y)
                data.write(data_list[i])

        
    time.sleep(0.1)

