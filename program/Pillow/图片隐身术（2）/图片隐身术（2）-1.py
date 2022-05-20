from PIL import Image
import numpy as np


img = input('文件路径(带后缀)：')
save = '.'.join([img.split('.')[0]+'_encrypted', img.split('.')[1]])

option = input('加密/解密：')

if option == '加密':
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

    pic = Image.open(img).convert('L')
    txt_ary = str2bin(txt_str)
    h,w = txt_ary.shape
    piece_ary = np.array(pic.crop((0, 0, w, h)))
    crypt_ary = txt_ary + piece_ary

    pic.paste(Image.fromarray(crypt_ary), (0,0))
    pic.save(save)
    print('加密完成')

elif option == '解密':
    original_pic = Image.open(img).convert('L')
    encrypted_pic = Image.open(save).convert('L')
    o_ary = np.array(original_pic)
    e_ary = np.array(encrypted_pic)
    crypt_ary = e_ary-o_ary
    
    txt_lst = [chr(int(''.join(str(list(i[0:7]))).replace(',', '').replace(' ', '')[
        1:-1],2)) for i in crypt_ary if not (i[0:7] == np.array([0, 0, 0, 0, 0, 0, 0])).all()]
    txt_str = ''.join(txt_lst)
    print('内容是：'+txt_str)