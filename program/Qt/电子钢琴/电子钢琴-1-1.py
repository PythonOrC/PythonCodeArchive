import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound
from ui_piano import Ui_Piano


class Piano(QMainWindow, Ui_Piano):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()

        self.show()

    def setup(self):
        self.keyboard_img = QPixmap('piano.jpg')
        self.lb_keyboard.setPixmap(self.keyboard_img)

        self.As = QSound('sound/A.wav')
        self.Bs = QSound('sound/B.wav')
        self.Cs = QSound('sound/C.wav')
        self.Ds = QSound('sound/D.wav')
        self.Es = QSound('sound/E.wav')
        self.Fs = QSound('sound/F.wav')
        self.Gs = QSound('sound/G.wav')
        self.CHs = QSound('sound/CH.wav')

        self.key_press_img = QPixmap('编程猫.png')

        self.label_a.setScaledContents(True)
        self.label_b.setScaledContents(True)
        self.label_c.setScaledContents(True)
        self.label_d.setScaledContents(True)
        self.label_e.setScaledContents(True)
        self.label_f.setScaledContents(True)
        self.label_g.setScaledContents(True)
        self.label_ch.setScaledContents(True)
        self.label_music.setScaledContents(True)

        self.pbtn.clicked.connect(self.select_music)
        self.resize(520, 320)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            self.Cs.play()
            self.label_c.setPixmap(self.key_press_img)

        elif event.key() == Qt.Key_2:
            self.Ds.play()
            self.label_d.setPixmap(self.key_press_img)

        elif event.key() == Qt.Key_3:
            self.Es.play()
            self.label_e.setPixmap(self.key_press_img)

        elif event.key() == Qt.Key_4:
            self.Fs.play()
            self.label_f.setPixmap(self.key_press_img)

        elif event.key() == Qt.Key_5:
            self.Gs.play()
            self.label_g.setPixmap(self.key_press_img)

        elif event.key() == Qt.Key_6:
            self.As.play()
            self.label_a.setPixmap(self.key_press_img)

        elif event.key() == Qt.Key_7:
            self.Bs.play()
            self.label_b.setPixmap(self.key_press_img)

        elif event.key() == Qt.Key_8:
            self.CHs.play()
            self.label_ch.setPixmap(self.key_press_img)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_1:
            self.label_c.setPixmap(None)
        elif event.key() == Qt.Key_2:
            self.label_d.setPixmap(None)
        elif event.key() == Qt.Key_3:
            self.label_e.setPixmap(None)
        elif event.key() == Qt.Key_4:
            self.label_f.setPixmap(None)
        elif event.key() == Qt.Key_5:
            self.label_g.setPixmap(None)
        elif event.key() == Qt.Key_6:
            self.label_a.setPixmap(None)
        elif event.key() == Qt.Key_7:
            self.label_b.setPixmap(None)
        elif event.key() == Qt.Key_8:
            self.label_ch.setPixmap(None)

    def select_music(self):
        file_path = QFileDialog.getOpenFileName(caption='选择乐谱', filter='(*jpg *.png)')
        if file_path[0]:
            self.file = file_path[0]
            music_img = QPixmap(self.file)
            self.label_music.setPixmap(music_img)
            self.resize(520, 700)
        else:
            self.label_music.setText('乐谱')
            self.resize(520, 320)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Piano()
    sys.exit(app.exec_())
