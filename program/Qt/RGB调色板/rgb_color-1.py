import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ui_rbg import Ui_RGB
from PIL import Image, ImageQt


class RGB(QMainWindow, Ui_RGB):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
        self.show()

    def setup(self):
        self.slider_r.valueChanged.connect(self.process)
        self.slider_g.valueChanged.connect(self.process)
        self.slider_b.valueChanged.connect(self.process)

        self.label.setScaledContents(True)

    def process(self):
        color_r = self.slider_r.value()
        color_g = self.slider_g.value()
        color_b = self.slider_b.value()
        self.label_r.setText(str(color_r))
        self.label_g.setText(str(color_g))
        self.label_b.setText(str(color_b))

        rgb = (color_r, color_g, color_b)
        self.lineEdit.setText(str(rgb))

        img = Image.new('RGBA', (100, 100), rgb)
        img = ImageQt.ImageQt(img)
        img = QPixmap.fromImage(img)
        self.label.setPixmap(img)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RGB()
    sys.exit(app.exec_())
