from PIL import Image
import numpy as np

txt_str = input('加密内容：')

def str2bin(txt_str):
    txt_asc = []
    txt_bin = []
    ltr_bin = []

    txt_asc = [ord(letter) for letter in txt_str]
    for num in txt_asc:
        tmp = list(bin(num)[2:])
        ltr_bin = [int(n) for n in tmp]
        txt_bin.append(ltr_bin)
    txt_ary = np.array(txt_bin)

    return(txt_ary)


img = '舞台.png'

pic = Image.open(img).convert('L')
txt_ary = str2bin(txt_str)
h,w = txt_ary.shape
piece_ary = np.array(pic.crop((0, 0, w, h)))
crypt_ary = txt_ary + piece_ary

pic.paste(Image.fromarray(crypt_ary), (0,0))
save = '.'.join([img.split('.')[0]+'_encrpyted', img.split('.')[1]])
pic.save(save)

