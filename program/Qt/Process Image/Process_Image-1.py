import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PIL import Image, ImageFilter, ImageQt
from ui_Process_Image import Ui_process_img
from sketch import to_sketch
from char import to_char


class ProcessImg(QMainWindow, Ui_process_img):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file = None
        self.img_temp = None
        self.filters = {
            '模糊滤镜': ImageFilter.BLUR,
            '轮廓滤镜': ImageFilter.CONTOUR,
            '边缘强化滤镜': ImageFilter.EDGE_ENHANCE,
            '浮雕滤镜': ImageFilter.EMBOSS,
            '锐化滤镜': ImageFilter.SHARPEN,
            '平滑滤镜': ImageFilter.SMOOTH,
        }

        self.pb_file.clicked.connect(self.select_file)
        self.pb_process.clicked.connect(self.process_img)
        self.pb_save_img.clicked.connect(self.save_img)
        self.lb_input_img.setScaledContents(True)
        self.lb_output_img.setScaledContents(True)
        self.show()

    def select_file(self):
        file_path = QFileDialog.getOpenFileName(caption='选择文件', filter='(*.jpg *.png)')
        if file_path[0]:
            self.file = file_path[0]
            print(self.file)
            img_pix = QPixmap(self.file)
            self.lb_input_img.setPixmap(img_pix)
            self.img_temp = None
        else:
            QMessageBox.warning(self, '注意', '请重新选择图片文件')

    def process_img(self):
        if self.img_temp:
            img = self.img_temp
        else:
            if self.file:
                img = Image.open(self.file)
            else:
                QMessageBox.warning(self, '注意', '请先选图片文件')
                return
        text = self.cb_filter_list.currentText()
        if '滤镜' in text:
            self.img_temp = img.filter(self.filters[text]).convert('RGBA')
        elif text == '素描风格转化':
            self.img_temp = to_sketch(img)
        elif text == '字符画风格转化':
            self.img_temp = to_char(img)
        img_qt = ImageQt.ImageQt(self.img_temp)
        img_pix = QPixmap.fromImage(img_qt)
        self.lb_output_img.setPixmap(img_pix)
        
    
    def save_img(self):
        if self.img_temp:
            file_path = QFileDialog.getSaveFileName(caption = '保存文件',filter = '(*.png)')
            if file_path[0]:
                save_path = file_path[0]
                self.img_temp.save(save_path)
            else:
                QMessageBox.warning(self, '注意', '请从新选择保存位置')
        else:
            QMessageBox.warning(self, '注意', '请先进行图像处理')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProcessImg()
    sys.exit(app.exec_())
