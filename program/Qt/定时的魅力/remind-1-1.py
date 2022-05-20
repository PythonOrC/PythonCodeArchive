import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from ui_remind import Ui_Remind
from PySide2.QtMultimedia import QSound

class Remind(QMainWindow, Ui_Remind):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()

    def setup(self):
        self.label.setScaledContents(True)
        img = QPixmap('water.jpg')
        self.label.setPixmap(img)
        self.sound_river = QSound('river.wav')
        self.sound_insect = QSound('day.wav')
        self.sound_river.setLoops(QSound.Infinite)
        self.sound_insect.setLoops(QSound.Infinite)

        self.work_time = 1000*2
        self.rest_time = 1000*5
        self.timer = QTimer()
        self.timer.singleShot(self.work_time, self.rest)

    def rest(self):
        self.sound_river.play()
        self.sound_insect.play()
        self.showMaximized()
        self.timer.singleShot(self.rest_time, self.work)

    def work(self):
        self.hide()
        self.sound_river.stop()
        self.sound_insect.stop()
        self.timer.singleShot(self.work_time, self.rest)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Remind()
    sys.exit(app.exec_())
