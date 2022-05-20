import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class Painter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()
        self.show()

    def setup(self):
        self.img = None
        self.material = None
        self.painter = QPainter()

    def paintEvent(self, event):
        if self.img:
            self.painter.begin(self)
            self.painter.drawPixmap(0, 0, self.img)
            self.painter.end()

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        if self.img and self.material:
            self.painter.begin(self.img)
            w = self.material.width()//2
            h = self.material.height()//2
            self.painter.drawPixmap(x-w, y-h, self.material)
            self.painter.end()
            self.update()
            

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            file, _ = QFileDialog.getOpenFileName(
                caption='选择原图', filter='(*.jpg *.png)')
            if file:
                self.img = QPixmap(file)
                self.backup = self.img.copy()
                width = self.img.width()
                height = self.img.height()
                self.resize(width, height)
        elif event.key() == Qt.Key_2:
            file, _ = QFileDialog.getOpenFileName(caption='选择素材', filter='(*.jpg *.png)')
            if file:
                self.material = QPixmap(file)
                self.setCursor(QCursor(self.material))
        
        elif event.key() == Qt.Key_3:
            if self.img:
                file, _ = QFileDialog.getSaveFileName(caption='保存结果', filter='(*.jpg *.png)')
                if file:
                    self.img.save(file)
                else:
                    print('Error')
        elif event.key() == Qt.Key_4:
            if self.backup and self.img:
                self.img = self.backup.copy()
                self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Painter()
    sys.exit(app.exec_())
