import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ui_限时编辑器 import Ui_Edit


class Edit(QMainWindow, Ui_Edit):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
        self.show()

    def setup(self):
        self.pushButton.setText('开始')
        self.pushButton.clicked.connect(self.start)
        self.textEdit.setText('点击按钮开始写作')
        self.textEdit.setReadOnly(True)

    def start(self):
        self.pushButton.setText('保存')
        self.pushButton.clicked.connect(self.save)
        self.textEdit.setText('')
        self.textEdit.setReadOnly(False)
        self.pushButton.setEnabled(False)

        timer = QTimer()
        timer.singleShot(1000*5, self.finish)

    def finish(self):
        self.pushButton.setEnabled(True)
        self.textEdit.setReadOnly(True)

    def save(self):
        file = QFileDialog.getSaveFileName(caption='保存写作内容', filter='*.txt')[0]
        print('opened')
        content = self.textEdit.toPlainText()
        print(type(content), content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            print('saved')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Edit()
    sys.exit(app.exec_())
