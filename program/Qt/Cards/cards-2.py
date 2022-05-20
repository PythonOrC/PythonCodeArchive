import sys
from PySide2.QtCore import *
from PySide2. QtGui import *
from PySide2.QtWidgets import *
from ui_cards import Ui_Cards


class MyCards(QMainWindow, Ui_Cards):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_button()
        self.init_img()
        self.show()
        self.clicked_num = 0
        self.match_img = {
            1:{
                'pb':None,
                'pb_img' : None
            },
            2:{
                'pb':None,
                'pb_img' :None
            },
        }
        self.first_clicked = True
        self.time = 0
        self.right_count = 0
        self.pb_img.buttonClicked.connect(self.pb_func)

    def init_button(self):
        pb_list = self.pb_img.buttons()
        for btn in pb_list:
            btn.setText('')
            btn.setIcon(QIcon('bg.png'))
            btn.setIconSize(QSize(150,150))
            btn.setCheckable(True)
    def init_img(self):
        import os
        import random
        images_type = ['.png','.jpg','.bmp','.jpeg']
        files = os.listdir('images')
        all_imgs = []
        for file in files:
            ext = os.path.splitext(file)[-1]
            if ext in images_type:
                all_imgs.append('images' + os.sep + file)
        random_imgs = random.sample(all_imgs,6)
        grid_imgs = random_imgs + random_imgs
        random.shuffle(grid_imgs)
        pb_list  =  self.pb_img.buttons()
        self.grids = dict(zip(pb_list,grid_imgs))
    def pb_func(self):
        if self.first_clicked:
            self.first_clicked = False
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)
        if self.clicked_num < 2:
            QApplication.processEvents()
            pb = self.pb_img.checkedButton()
            if pb != self.match_img[1]['pb']:
                self.clicked_num += 1
                pb.setIcon(QIcon(self.grids[pb]))
                self.match_img[self.clicked_num]['pb'] = pb
                self.match_img[self.clicked_num]['pb_img'] = self.grids[pb]
                timer = QTimer()
                timer.singleShot(500, self.judge)
        
    def judge(self):
        if self.clicked_num == 2:
            self.clicked_num = 0
            if self.match_img[1]['pb_img'] != self.match_img[2]['pb_img']:
                self.match_img[1]['pb'].setIcon(QIcon('bg.png'))
                self.match_img[2]['pb'].setIcon(QIcon('bg.png'))
            else:
                self.right_count += 1
                if self.right_count == 6:
                    self.timer.stop()
    def update_time(self):
        self.time += 1
        self.lcd_time.display(self.time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyCards()
    sys.exit(app.exec_())
