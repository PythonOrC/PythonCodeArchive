import sys

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import *
from ui_timer import Ui_Timer


class MyTimer(QMainWindow, Ui_Timer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_set()
        self.show()
        # 绑定信号与槽函数
        self.pbtn_start.clicked.connect(self.start_time)
        self.pbtn_stop.clicked.connect(self.stop_time)
        self.timer.timeout.connect(self.update_time)

    def init_set(self):
        self.time = 0
        self.timer = QTimer()
        # 启用开始计时按钮
        self.pbtn_start.setEnabled(True)
        # 禁用停止计时开妞
        self.pbtn_stop.setEnabled(False)

    def start_time(self):
        QApplication.processEvents()
        # 显示时间
        self.time = 0
        self.lcd_time.display(self.time)
        # 启用停止计时按钮
        self.pbtn_stop.setEnabled(True)
        # 禁用开始计时按钮
        self.pbtn_start.setEnabled(False)
        # 延时1s
        self.timer.start(1000)

    def stop_time(self):
        QApplication.processEvents()
        # 启用开始计时按钮
        self.pbtn_start.setEnabled(True)
        # 禁用停止计时按钮
        self.pbtn_stop.setEnabled(False)
        # 延时1s
        self.timer.stop()

    def update_time(self):
        QApplication.processEvents()
        # 显示时间
        self.time += 1
        self.lcd_time.display(self.time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyTimer()
    sys.exit(app.exec_())
