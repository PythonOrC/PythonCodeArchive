from vpython import *

red = cylinder(pos=vec(0, 0, 0), radius=1, axis=vec(1, 0, 0), color=color.red)
yellow = red.clone(pos=vec(0, -2.5, 0), color=color.yellow)
green = red.clone(pos=vec(0, -5, 0), color=color.green)
shell = box(pos=vec(0, -2.5, 0), size=vec(0.8, 8, 3))
post = cylinder(pos=vec(0, -6.5, 0), radius=0.4, axis=vec(0, -15, 0))
base = cylinder(pos=vec(0, -21.5, 0), radius=4, axis=vec(0, 1, 0))
red_time = 30
green_time = 10
yellow_time = 3

def switch_to(from_light, to_light, time):
    from_light.emissive = False
    to_light.emissive = True
    sleep(time)
cnt = 0
while True:
    switch_to(red,green,green_time)
    switch_to(green, yellow, yellow_time)
    switch_to(yellow, red, red_time)
