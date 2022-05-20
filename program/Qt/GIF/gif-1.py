import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ui_gif import Ui_gif
import random
from PySide2.QtMultimedia import QSound


class GIF(QMainWindow, Ui_gif):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
        self.show()

    def setup(self):
        self.speed = 100
        self.label.setScaledContents(True)
        # img = QPixmap('bcm.jpg')
        # self.label.setPixmap(img)
        self.movie = QMovie()
        self.movie.setFileName('lottery.gif')
        self.label.setMovie(self.movie)
        self.movie.jumpToFrame(0)
        self.sound = QSound('lottery.wav')

        self.pbtn_play.clicked.connect(self.play)
        self.pbtn_pause.clicked.connect(self.pause)
        self.pbtn_fast.clicked.connect(self.fast)
        self.pbtn_slow.clicked.connect(self.slow)

    def slow(self):
        self.speed -= 20
        self.movie.setSpeed(self.speed)

    def fast(self):
        self.speed += 100
        self.movie.setSpeed(self.speed)

    def pause(self):
        self.movie.setPaused(True)
        number = random.randint(0, 10)
        self.label.setText(str(number))
        self.sound.stop()

    def play(self):
        self.movie.setSpeed(500)
        self.movie.start()
        self.sound.play()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_P:
            self.playing = not self.playing

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GIF()
    sys.exit(app.exec_())
