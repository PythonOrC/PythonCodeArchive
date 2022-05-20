import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class Tray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.setup()
        self.show()

    def setup(self):
        self.index = 0
        self.tips = ['Click on me', 'Hello', 'Meow']
        self.icon_sit = QIcon('sit.png')
        self.icon_stand = QIcon('stand.png')

        self.setIcon(self.icon_sit)
        self.setToolTip('Meow')
        self.activated.connect(self.process)
        self.sound1 = QSound('sound1.wav')
        self.sound2 = QSound('sound2.wav')

        self.timer = QTimer()
        self.icons = ['images/0.png', 'images/1.png',
                      'images/2.png', 'images/3.png', 'images/4.png']
        self.icon_index = 0
        self.change_icon()

    def process(self, key):
        if key == self.Trigger:
            self.sound1.play()
            self.setIcon(self.icon_sit)
        elif key == self.MiddleClick:
            pass
        elif key == self.Context:
            self.sound2.play()
            self.setIcon(self.icon_stand)
        self.setToolTip(self.tips[self.index % len(self.tips)])
        self.index += 1

    def change_icon(self):
        self.setIcon(QIcon(self.icons[self.icon_index % len(self.icons)]))
        self.icon_index += 1
        self.timer.singleShot(100, self.change_icon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tray = Tray()
    sys.exit(app.exec_())
