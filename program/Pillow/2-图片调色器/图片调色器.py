from PIL import Image
from PySide2.QtWidgets import *
from ui_图片调色器 import Ui_MainWindow
import sys
class PictureADJ(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
        self.show()
    def setup(self):
        self.open_pbtn.clicked.connect(self.open_img)
        self.render_pbtn.clicked.connect(self.adj_pic)
    def open_img(self):
        self.data_file, _ = QFileDialog.getOpenFileName(caption = '选择图像文件', filter='(*.png *.jpg)')
        self.img = Image.open(self.data_file).convert('RGB')
        self.if_open_lb.setText(f'{self.data_file}获取成功')

    def adj_pic(self):
        r, g, b = self.r_slider.value(), self.g_slider.value(), self.b_slider.value()
        prev_progress = 0
        w, h = self.img.size
        for y in range(h):
            for x in range(w):
                RGB_value = self.img.getpixel((x, y))
                new_color = list(RGB_value)
                new_color[0] += r
                new_color[1] += g
                new_color[2] += b
                self.img.putpixel((x, y), tuple(new_color))
            progress = int((y+1)*100/h)
            if progress != prev_progress:
                self.progressBar.setValue(progress)
                prev_progress = progress
        self.img.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PictureADJ()
    sys.exit(app.exec_())


