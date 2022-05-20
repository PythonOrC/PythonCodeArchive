from vpython import *

x = curve(vec(0, 0, 0), vec(10, 0, 0), color=color.red)
y = curve(vec(0, 0, 0), vec(0, 10, 0), color=color.green)
z = curve(vec(0, 0, 0), vec(0, 0, 10), color=color.blue)
box(opacity=0.5)
box(pos=vec(3, 0, 0), size=vec(4, 2, 1), color=color.red)
