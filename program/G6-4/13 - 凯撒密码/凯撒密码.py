def caesar_cipher(text, shift):
    result = ""
    for i in text:
        result += chr((ord(i) + shift) % 128)

    return result


if input("1. 加密\n2. 解密\n") == 1:
    cipher = 1
else:
    cipher = -1

print(caesar_cipher(input("文字："), cipher * int(input("位移："))))
