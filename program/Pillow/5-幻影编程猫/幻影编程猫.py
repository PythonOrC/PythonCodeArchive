from PIL import Image
import numpy as np
import time
start = time.time()

codemao = Image.open('codemao.jpg').convert('RGB')

w, h = codemao.size

R, G, B = np.array(codemao), np.array(codemao), np.array(codemao)

R[:, :, 1], R[:, :, 2] = 0, 0
G[:, :, 0], G[:, :, 2] = 0, 0
B[:, :, 0], B[:, :, 1] = 0, 0

# r = Image.fromarray(R)
# g = Image.fromarray(G)
# b = Image.fromarray(B)
GB = G+B
gb = Image.fromarray(GB)
temp = Image.new('RGB', codemao.size,(0,0,0))
temp.paste(gb, (80,80))
gb_off = np.array(temp)
# g_off = Image.new('RGB', codemao.size,(0, 0, 0))
# g_off.paste(g, (-80, -80))
# G_off = np.array(g_off)

res = Image.fromarray(R+GB_off)

res.show()

print(time.time()-start)
