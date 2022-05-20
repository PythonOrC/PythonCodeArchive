import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class Tray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.setup()
        self.add_menu()
        self.show()
    
    def setup(self):
        self.window = Window()
        self.icons = ['sit.png', 'stand.png']
        self.setIcon(QIcon(self.icons[0]))
        self.icon_index = 1


    def add_menu(self):
        self.menu = QMenu()
        action_print = QAction('打印', self, triggered=self.trigger_print)
        action_pose = QAction('切换站姿', self, triggered=self.trigger_pose)
        action_window = QAction('打开窗口', self, triggered=self.window.show_window)
        action_quit = QAction('退出', self, triggered=self.trigger_quit)
        
        self.menu.addAction(action_print)
        self.menu.addAction(action_pose)
        self.menu.addAction(action_quit)
        self.menu.addAction(action_window)

        self.setContextMenu(self.menu)
    
    def trigger_print(self):
        print('print')
    
    def trigger_pose(self):
        self.setIcon(QIcon(self.icons[self.icon_index % len(self.icons)]))
        self.icon_index += 1

    def trigger_quit(self):
        self.hide()
        sys.exit()
    
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def show_window(self):
        self.show()


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        self.show_tray()

    def show_tray(self):
        self.tray = Tray()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #tray = Tray()
    window = Window2()
    sys.exit(app.exec_())
