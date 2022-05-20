from PIL import Image, ImageOps, ImageFilter

def to_sketch(img):
    width, height = img.size


    img_gray = img.convert('L')

    img_invert = ImageOps.invert(img_gray)

    img_gaussian = img_invert.filter(ImageFilter.GaussianBlur(5))

    for x in range(width):
        for y in range(height):
            pos = (x, y)
            A = img_gray.getpixel(pos)
            B = img_gaussian.getpixel(pos)

            img_gray.putpixel(pos, min(int(A+A*B/(255-B)), 255))
    return img_gray

if __name__ == "__main__":
    img = Image.open("bcm.jpg")
    to_sketch(img).save("bcm_sketch.jpg")