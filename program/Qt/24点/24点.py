import sys
from PySide2 import QtWidgets, QtCore
from ui_24点 import Ui_MainWindow
import random

class Game(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
        self.show()

    def setup(self):
        num_list = [str(random.randint(1, 10)) for i in range(4)]
        cards = ['self.pbtn_'+str(i) for i in range(1,5)]
        for i in range(4):
            eval(cards[i]).setText(num_list[i])
        print(num_list)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.verify()
        
    def verify(self):
        result = eval(self.lineEdit.text())
        if result == 24:
            print('correct')
            self.setup()
            self.lineEdit.setText('')
        else:
            print('incorrect')
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Game()
    sys.exit(app.exec_())
