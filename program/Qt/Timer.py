import sys
from PySide2.QtCore import *
from PySide2. QtGui import *
from PySide2.QtWidgets import *
from ui_timer import Ui_Timer


class Timer(QMainWindow, Ui_Timer):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.timer = QTimer()
        self.time = 0
        self.pb_start.setEnabled(True)
        self.pb_stop.setEnabled(False)
        self.show()
        self.pb_start.clicked.connect(self.start_timer)
        self.pb_stop.clicked.connect(self.stop_timer)
        self.timer.timeout.connect(self.counting)
    
    def start_timer(self):
        QApplication.processEvents()
        self.time = 0
        self.lcd_timer.display(self.time)
        self.pb_start.setEnabled(False)
        self.pb_stop.setEnabled(True)
        self.timer.start(1000)

    def counting(self):
        QApplication.processEvents()
        self.time += 1
        self.lcd_timer.display(self.time)

    def stop_timer(self):
        QApplication.processEvents()
        self.pb_start.setEnabled(True)
        self.pb_stop.setEnabled(False)
        self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Timer()
    sys.exit(app.exec_())
