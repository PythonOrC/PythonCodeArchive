from vpython import *
scene.background = color.white
target = box(size=vec(9, 9, 0.5), texture="target.png")
ball = sphere(pos=vec(0, -4.5, 10), radius=1, texture="ball.png")
sleep(3)
v=vec(0,1.5,-10)
dt = 0.02
while ball.pos.z > 1.25:
    rate(50)
    ball.pos += v*dt
    