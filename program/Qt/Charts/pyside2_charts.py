import sys
from PySide2.QtWidgets import *
from ui_charts import Ui_Charts

class MyCharts(QMainWindow, Ui_Charts):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pb_data.clicked.connect(self.select_file)
    def select_file(self):
        self.lb_info.setText('我被单击了')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyCharts()
    sys.exit(app.exec_())