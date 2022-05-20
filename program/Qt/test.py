import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PIL import Image, ImageFilter, ImageQt
from ui_filter import Ui_process_img


class ProcessImg(QMainWindow, Ui_process_img):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file = None
        self.filters = {
            '模糊滤镜': ImageFilter.BLUR,
            '轮廓滤镜': ImageFilter.CONTOUR,
            '边缘强化滤镜': ImageFilter.EDGE_ENHANCE,
            '浮雕滤镜': ImageFilter.EMBOSS,
            '锐化滤镜': ImageFilter.SHARPEN,
            '平滑滤镜': ImageFilter.SMOOTH,
        }

        self.pbtn_file.clicked.connect(self.select_file)
        self.pb_process.clicked.connect(self.process_img)
        self.lb_input_img.setScaledContents(True)
        self.lb_output_img.setScaledContents(True)
        self.show()

    def select_file(self):
        file_path = QFileDialog.getOpenFileName(caption='选择文件', filter='(.*.jpg *png)')
        if file_path[0]:
            self.file = file_path[0]
            print(self.file)
            img_pix = QPixmap(self.file)
            self.lb_input_img.setPixmap(img_pix)
        else:
            print('请重新选择图片文件')

    def process_img(self):
        img = Image.open(self.file)
        text = self.cb_filter_list.currentText()
        print(self.filters[text])
        img_temp = img.filter(self.filters[text]).convert('RGBA')
        img_qt = ImageQt.ImageQt(img_temp)
        img_pix = QPixmap.fromImage(img_qt)
        self.lb_output_img.setPixmap(img_pix)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProcessImg()
    sys.exit(app.exec_())
