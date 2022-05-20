from PIL import Image, ImageQt
import random
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys


class Pic():
    def __init__(self):
        self.color_out = self.random_color()
        self.board = Image.new('HSV', (500, 500), self.color_out)
        self.rand_x, self.rand_y = random.randint(
            0, 9)*50, random.randint(0, 9)*50
        self.gen_pic()

    def random_color(self):
        return (random.randint(0, 360), random.randint(0, 255), 255)

    def color_in(self, color_out):
        self.res = list(color_out)
        self.res[0] += random.randint(10, 15)
        self.res = tuple(self.res)
        return self.res

    def color_bright(self, color_out):
        self.res = list(color_out)
        self.res[2] -= random.randint(0, 15)
        self.res = tuple(self.res)
        return self.res

    def gen_pic(self):
        for y in range(0, 500, 50):
            for x in range(0, 500, 50):
                if x == self.rand_x and y == self.rand_y:
                    new_block = Image.new(
                        'HSV', (50, 50), self.color_in(self.color_out))
                    self.board.paste(new_block, (x, y))
                else:
                    new_block = Image.new(
                        'HSV', (50, 50), self.color_bright(self.color_out))
                    self.board.paste(new_block, (x, y))
        self.board = self.board.convert('RGBA')

class OpsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()
        self.show()
    
    def setup(self):
        self.new_pic()
        w,h = self.img.width(), self.img.height()
        self.resize(w,h)
        self.painter = QPainter()


    def new_pic(self):
        self.pic = Pic()
        self.img = ImageQt.ImageQt(self.pic.board)
        self.img = QPixmap.fromImage(self.img)

    def paintEvent(self,event):
        self.painter.begin(self)
        self.painter.drawPixmap(0,0,self.img)
        self.painter.end()

    def mousePressEvent(self, event):
        x,y = event.x(),event.y()
        tar_x,tar_y = self.pic.rand_x, self.pic.rand_y
        if x>=tar_x and x<=tar_x+50 and y>=tar_y and y<tar_y+50:
            self.new_pic()
            self.update()
            print('正确')
        else:
            print(f'错误，正确的在第{(self.pic.rand_x//50)+1}行，第{(self.pic.rand_y//50)+1}列。')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OpsWindow()
    sys.exit(app.exec_())
