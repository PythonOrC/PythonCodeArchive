from PIL import Image
import random


def random_color():
    return (random.randint(0, 360), random.randint(0, 255), 255)


color_out = random_color()

board = Image.new('HSV', (500, 500), color_out)
rand_x, rand_y = random.randint(0, 9)*50, random.randint(0, 9)*50


def color_in(color_out):
    res = list(color_out)
    res[0] += random.randint(10, 15)
    res = tuple(res)
    return res


def color_bright(color_out):
    res = list(color_out)
    res[2] -= random.randint(0, 15)
    res = tuple(res)
    return res


for y in range(0, 500, 50):
    for x in range(0, 500, 50):
        if x == rand_x and y == rand_y:
            new_block = Image.new('HSV', (50, 50), color_in(color_out))
            board.paste(new_block, (x, y))
        else:
            new_block = Image.new('HSV', (50, 50), color_bright(color_out))
            board.paste(new_block, (x, y))

board.show()
