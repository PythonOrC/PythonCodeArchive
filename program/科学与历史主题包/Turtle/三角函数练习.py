import math

AB = 50
a = 30
AC = AB * math.sin(math.radians(a))
BC = AB * math.cos(math.radians(a))
print('AC: {}, BC: {}'.format(AC, BC))
print('AC: %f, BC: %f', % (AC,BC))