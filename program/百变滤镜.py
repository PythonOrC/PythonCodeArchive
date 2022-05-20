#万能滤镜
# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np

img = Image.open ('tower.png')
rgb = np.asarray(img, dtype = 'int')

r = rgb[:,:,0]
g = rgb[:,:,1]
b = rgb[:,:,2]
a = rgb[:,:,3]

F = np.array([[1,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]])

new_r = F[0][0]*r + F[0][1]*g + F[0][2]*b + F[0][3]*a + F[0][4]
new_g = F[1][0]*r + F[1][1]*g + F[1][2]*b + F[1][3]*a + F[1][4]
new_b = F[2][0]*r + F[2][1]*g + F[2][2]*b + F[2][3]*a + F[2][4]
new_a = F[3][0]*r + F[3][1]*g + F[3][2]*b + F[3][3]*a + F[3][4]

y,x = r.shape

im = Image.new('RGBA',(x,y))

for j in range(0,x):
	for i in range(0,y):
		im.paste(((int(new_r[i,j]),int(new_g[i,j]),int(new_b[i,j]),int(new_a[i,j]))),(j,i,j+1,i+1))

im.show('result.png')
