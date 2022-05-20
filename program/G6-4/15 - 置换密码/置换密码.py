from random import shuffle
from math import ceil


def print_str(content, num):
    line = ""
    for i in range(len(content)):
        line += content[i]
        if i % num == num - 1:
            print(line)
            line = ""


def encrypt(content, cols):
    cipher = ""

    length = len(content)
    rows = ceil(length / cols)
    char_len = rows * cols - length
    content += "@" * char_len
    print_str(content, cols)

    keys = list(range(1, cols + 1))
    shuffle(keys)
    for col in keys:
        for row in range(rows):
            ind = row * cols + (col - 1)
            cipher += content[ind]

    return cipher, keys


def decrypt(cipher, keys):
    length = len(cipher)
    cols = len(keys)
    rows = ceil(length / cols)
    plaintext = [""] * length
    num = 0
    for col in keys:
        for row in range(rows):
            ind = row * cols + (col - 1)
            if cipher[num] != "@":
                plaintext[ind] = cipher[num]
            num += 1
    return "".join(plaintext)


content = "hello-codemao!"
cols = 5
cipher, keys = encrypt(content, cols)
print("密文：", cipher, "密钥：", keys)
print("明文：", decrypt(cipher, keys))
