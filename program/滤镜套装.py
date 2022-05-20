#滤镜套装
# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np

img = Image.open('tower.png')
rgb = np.asarray(img, dtype = 'int')

r = rgb[:,:,0]
g = rgb[:,:,1]
b = rgb[:,:,2]
a = rgb[:,:,3]

			# 1: 绿色
F = np.array([[[1,0,0,0,50],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]],
            # 2: 紫色
              [[1,0,0,0,50],
               [0,2,0,0,0],
               [0,0,0,1,0],
               [0,0,0,1,0]],
             # 3: 黄色
		      [[2,0,0,0,0],
		       [0,1,0,0,50],
		       [0,0,0,1,0]],
		     # 4: 红色
			  [[2,0,0,0,0],
			  [0,1,0,0,0],
			  [0,0,1,0,0],
			  [0,0,0,1,0]]])
	
def filter(model):		  
	new_r = F[model-1][0][0]*r + F[model-1][0][1]*g + F[model-1][0][2]*b + F[model-1][0][3]*a + F[model-1][0][4]
	new_g = F[model-1][1][0]*r + F[model-1][1][1]*g + F[model-1][1][2]*b + F[model-1][1][3]*a + F[model-1][1][4]
	new_b = F[model-1][2][0]*r + F[model-1][2][1]*g + F[model-1][2][2]*b + F[model-1][2][3]*a + F[model-1][2][4]
	new_a = F[model-1][3][0]*r + F[model-1][3][1]*g + F[model-1][3][2]*b + F[model-1][3][3]*a + F[model-1][3][4]

	y,x = r.shape

	im = Image.new('RGBA',(x,y))

	for j in range(0,x):
		for i in range(0,y):
			im.paste(((int(new_r[i,j]),int(new_g[i,j]),int(new_b[i,j]),int(new_a[i,j]))),(j,i,j+1,i+1))

	im.show('result.png')

filter(4)
