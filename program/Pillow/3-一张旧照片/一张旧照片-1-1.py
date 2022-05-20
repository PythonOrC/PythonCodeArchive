from PIL import Image, ImageOps, ImageEnhance
from PySide2.QtWidgets import *
from ui_picture_adj import Ui_MainWindow
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
        self.save_pbtn.clicked.connect(self.save_img)

    def open_img(self):
        self.data_file, _ = QFileDialog.getOpenFileName(
            caption='选择图像文件', filter='(*.png *.jpg)')
        self.if_open_lb.setText(f'{self.data_file} 获取成功')

    def save_img(self):
        self.save_file, _ = QFileDialog.getSaveFileName(cation='保存图像文件', filter='(*.ing *.jpg)')
        self.img.save(self.save_file)

    def adj_pic(self):
        self.img = Image.open(self.data_file).convert('RGB')
        if self.checkBox.isChecked():
            self.img = ImageOps.invert(self.img)
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

        contrast = self.contrast_slider.value()
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(contrast/100)

        bright = self.brightness_slider.value()
        enhancer = ImageEnhance.Brightness(self.img)
        self.img = enhancer.enhance(bright/100)
        self.img.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PictureADJ()
    sys.exit(app.exec_())



