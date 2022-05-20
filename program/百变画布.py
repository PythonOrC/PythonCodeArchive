#百变画布
#-*- coding: utf-8 -*-
from PIL import Image
import numpy as np

img = Image.open('tower.png')
rgb = np.asarray(img, dtype = 'int')

new_r = rgb[:,:,0]
new_g = rgb[:,:,1]
new_b = rgb[:,:,2]
new_a = rgb[:,:,3]

new_r[:] = 255
new_g[:] = 0
new_b[:] = 100
new_a[:] = 255

y,x = new_r.shape
im = Image.new('RGBA',(x,y))

for j in range(0,x):
	for i in range(0,y):
		im.paste(((int(new_r[i,j]),int(new_g[i,j]),int(new_b[i,j]),int(new_a[i,j]))),(j,i,j+1,i+1))
		
im.save('result_255000100.png')
