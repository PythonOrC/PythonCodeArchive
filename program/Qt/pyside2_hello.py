import sys
from PySide2.QtWidgets import *
from ui_hello import Ui_hello


class Hello(QMainWindow,Ui_hello):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Hello()
    sys.exit(app.exec_())

