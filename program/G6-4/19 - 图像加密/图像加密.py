from PIL import Image
from numpy import array, uint8
from random import randint


def pic_to_list(path):
    pic = Image.open(path).convert("RGB")
    w, h = pic.size
    pic_array = array(pic)
    pic_list = pic_array.tolist()
    return pic_list, w, h


def get_key(row, col):
    keys = []
    for i in range(row):
        keys.append(randint(1, col))
    return keys


def encrypt(picture, w, h):
    keys = get_key(w, h)
    for i in range(h):
        key = keys[i]
        list_a = picture[i][:key]
        list_b = picture[i][key:]
        picture[i][: w - key] = list_b
        picture[i][w - key :] = list_a
    return picture, keys


def decrypt(picture, w, h, keys):
    for i in range(h):
        key = keys[i]
        list_a = picture[i][: w - key]
        list_b = picture[i][w - key :]
        picture[i][:key] = list_b
        picture[i][key:] = list_a
    return picture


def list_to_pic(RGB_list, path):
    arr = array(RGB_list)
    pic = Image.fromarray(uint8(arr))
    pic.save(path)
    pic.show()


# encrypt
en_list, keys = encrypt(*pic_to_list("图片.png"))
list_to_pic(en_list, "加密图片.png")

# decrypt
de_list = decrypt(*pic_to_list("加密图片.png"), keys)
list_to_pic(de_list, "解密图片.png")
