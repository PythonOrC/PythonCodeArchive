from captcha.image import ImageCaptcha
import random

def rndChar():
    return chr(random.randint(65,90))

rnd = ''.join([rndChar() for i in range(4)])
print(rnd)

image = ImageCaptcha()
image.write(rnd, 'out.png')

ans = input('验证码：').lower()
if ans == rnd.lower():
    print('正确')