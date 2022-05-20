from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import collections

pic = Image.open('bag.png').convert('RGB')
w, h = pic.size
block = 50

board = Image.new('RGB', pic.size)

for y in range(0, h, block):
    for x in range(0, w, block):
        temp = pic.crop((x,y,x+block, y+block))
        temp_list = list(temp.getdata())
        max_color = collections.Counter(temp_list).most_common()[0][0]
        temp_past = Image.new('RGB',temp.size, max_color)
        print(max_color)
        board.paste(temp_past, (x,y))

board.show()